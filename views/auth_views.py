from datetime import timedelta
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)
from app import db
from models import User
from schemas import UserSchema, UserMinimalSchema


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.authorization
    username = data.username
    password = data.password

    usuario = User.query.filter_by(username=username).first()
    
    if usuario and check_password_hash(
        pwhash=usuario.password_hash, password=password
    ):
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=2000),
            additional_claims=dict(
                administrador=usuario.is_admin
            )
        )

        return jsonify({'Token':access_token}) 

    return jsonify(Mensaje="El usuario y la contraseña al parecer no coinciden")


@auth_bp.route('/users', methods=['GET', 'POST'])
@jwt_required()
def users():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if request.method == 'POST':
        if administrador is True:
            data = request.get_json()
            username = data.get('usuario')
            password = data.get('contrasenia')

            try:
                nuevo_usuario = User(
                    username=username,
                    password_hash=generate_password_hash(password),
                    is_admin=False,
                )
                db.session.add(nuevo_usuario)
                db.session.commit()
                return jsonify(
                    {
                    "Mensaje":"Usuario creado correctamente",
                    "Usuario": nuevo_usuario.to_dict()
                    }
                )
            except Exception as e:
                db.session.rollback()
                return jsonify(
                    {
                    "Mensaje":"Fallo la creacion del nuevo usuario",
                    "Error": str(e)
                    }
                )
        else:
            return jsonify(Mensaje= "Solo el admin puede crear nuevos usuarios")
    
    usuarios = User.query.all()
    usuarios_dict = [] 
    for usuario in usuarios:
        usuarios_dict.append(usuario.to_dict())

    return jsonify(usuarios_dict)

@auth_bp.route('/users/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_users(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje":"Solo el admin puede eliminar usuarios"})
    
    usuario = User.query.get(id)
    if not usuario:
        return jsonify({"Mensaje":"Usuario no encontrado"}), 404 

    try:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"Mensaje":"Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje":"Fallo al eliminar el usuario", "Error": str(e)}), 500 
    
@auth_bp.route('/users/<int:id>/update', methods=['PUT'])
@jwt_required()
def update_user(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if administrador is not True:
        return jsonify({"Mensaje":"No tienes permiso para actualizar"})
    
    data = request.get_json()
    username = data.get('usuario')
    password = data.get('contrasenia')

    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"Mensaje":"Usuario no encontrado"}), 404
        
        user.username = username if username else user.username
        user.password_hash = generate_password_hash(password) if password else user.password_hash

        db.session.commit()
        return jsonify({"Mesnaje":"Usuario actualizado correctamente", "Usuario" : user.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje":"Error al actualizar el usuario: " + str(e)}), 500
    
    
