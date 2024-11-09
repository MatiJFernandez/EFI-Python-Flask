from flask import Blueprint, request, jsonify
from flask_jwt_extended import (get_jwt, jwt_required)
from app import db  
from models import  Accesorio
from schemas import AccesorioSchema 
from services.accesorio_service import AccesorioService
from repositories.accesorio_repositories import AccesorioRepositories
#from forms import AccesorioForm 

accesorio_bp = Blueprint('accesorio', __name__) 

@accesorio_bp.route('/accesorios_list', methods=['GET'])
@jwt_required()
def accesorios_list():
    accesorios_services = AccesorioService(AccesorioRepositories())
    accesorios = accesorios_services.get_all()

    accesorio_schema = AccesorioSchema(many=True)
    accesorios_serializados = accesorio_schema.dump(accesorios) 

    return jsonify({'accesorios': accesorios_serializados})

@accesorio_bp.route('/accesorios', methods=['POST', 'GET'])
@jwt_required()
def accesorios():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear accesorios"}), 403

    accesorio_service = AccesorioService(AccesorioRepositories())

    if request.method == 'POST':
        data = request.get_json()  
        nombre = data.get('nombre') 
        

        if not nombre:
            return jsonify({"Mensaje": "El nombre del accesorio es obligatorio"}), 400

        nuevo_accesorio = accesorio_service.create(nombre)
        accesorio_schema = AccesorioSchema()

        return jsonify({
            "Mensaje": "accesorio creado exitosamente",
            "accesorio": accesorio_schema.dump(nuevo_accesorio)
        }), 201

@accesorio_bp.route("/accesorios/<id>/editar", methods=['PUT'])
@jwt_required()
def accesorios_editar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para editar el accesorio"}), 403

    accesorio = Accesorio.query.get_or_404(id)

    if request.method == 'PUT':
        nombre = request.json.get('nombre')
        
        
        if not nombre:
            return jsonify({"Mensaje": "El campo 'nombre' es obligatorio"}), 400
        accesorio.nombre = nombre

        db.session.commit()

        accesorio_schema = AccesorioSchema()
        accesorio_serializada = accesorio_schema.dump(accesorio)

        return jsonify({
            "Mensaje": "El accesorio esta editado con éxito",
            'accesorio': accesorio_serializada
        }), 200

    accesorio_schema = AccesorioSchema()
    accesorio_serializada = accesorio_schema.dump(accesorio)

    return jsonify({'accesorio': accesorio_serializada})

@accesorio_bp.route('/accesorio/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_accesorio(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el administrador puede eliminar accesorios"}), 403

    accesorio = Accesorio.query.get(id)
    if not accesorio:
        return jsonify({"Mensaje": "Accesorio no encontrado"}), 404

    try:
        db.session.delete(accesorio)
        db.session.commit()
        return jsonify({"Mensaje": "Accesorio eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al eliminar la accesorio", "Error": str(e)}), 500
