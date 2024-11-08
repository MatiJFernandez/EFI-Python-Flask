from flask import Blueprint, request, jsonify
from flask_jwt_extended import (get_jwt, jwt_required)

from app import db  
from models import  Marca
from schemas import MarcaSchema 
from services.marca_service import MarcaService
from repositories.marca_repositories import MarcaRepositories
from forms import MarcaForm

marca_bp = Blueprint('marca', __name__)

@marca_bp.route('/marcas_list', methods=['GET'])
def marcas_list():
    marcas = Marca.query.all()
    return MarcaSchema().dump(marcas, many=True)

@marca_bp.route('/marcas', methods=['POST', 'GET'])
@jwt_required()
def marcas():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear marcas"}), 403

    marca_service = MarcaService(MarcaRepositories())

    if request.method == 'POST':
        data = request.get_json()  
        nombre = data.get('nombre') 
        modelo = data.get('modelo') 

        if not nombre:
            return jsonify({"Mensaje": "El nombre de la marca es obligatorio"}), 400

        if not modelo:
            return jsonify({"Mensaje": "El modelo de la marca es obligatorio"}), 400
        
        nueva_marca = marca_service.create(nombre, modelo)
        marca_schema = MarcaSchema()

        # Devolver directamente una respuesta JSON en lugar de hacer una redirección
        return jsonify({
            "Mensaje": "Marca creada exitosamente",
            "marca": marca_schema.dump(nueva_marca)
        }), 201

@marca_bp.route("/marcas/<id>/editar", methods=['PUT'])
@jwt_required()
def marcas_editar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para editar el marca"}), 403

    marca = Marca.query.get_or_404(id)

    if request.method == 'PUT':
        nombre = request.json.get('nombre')
        modelo = request.json.get('modelo')
        
        if not nombre:
            return jsonify({"Mensaje": "El campo 'nombre' es obligatorio"}), 400
        marca.nombre = nombre

        if not modelo:
            return jsonify({"Mensaje": "El campo 'modelo' es obligatorio"}), 400
        marca.modelo = modelo
        
        db.session.commit()

        marca_schema = MarcaSchema()
        marca_serializada = marca_schema.dump(marca)

        return jsonify({
            "Mensaje": "El marca esta editado con éxito",
            'marca': marca_serializada
        }), 200

    marca_schema = MarcaSchema()
    marca_serializada = marca_schema.dump(marca)

    return jsonify({'marca': marca_serializada})

@marca_bp.route('/marca/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_marca(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el administrador puede eliminar marcas"}), 403

    marca = Marca.query.get(id)
    if not marca:
        return jsonify({"Mensaje": "Marca no encontrado"}), 404

    try:
        db.session.delete(marca)
        db.session.commit()
        return jsonify({"Mensaje": "Marca eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al eliminar la marca", "Error": str(e)}), 500
