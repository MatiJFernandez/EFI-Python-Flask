from flask import Blueprint, request, make_response, jsonify
from sqlalchemy.exc import IntegrityError

from app import db
from models import Celular, Marca

from schemas import MarcaSchema, CelularSchema 

celular_bp = Blueprint('celular', __name__)

@celular_bp.route('/celulares_list', methods=['GET'])
def celulares_list():
    celulares = Celular.query.all()
    return CelularSchema().dump(celulares, many=True)


@celular_bp.route('/celulares', methods=['GET', 'POST'])
def celulares():
    if request.method == 'POST':
        data = request.get_json()
        errors = CelularSchema().validate(data)
        if errors:
            return make_response(jsonify(errors))
        
        # Verificar si la marca existe
        marca_id = data.get('marca_id')
        marca = Marca.query.get(marca_id)
        if not marca:
            return jsonify({"Error": f"La marca con id {marca_id} no existe."})
        
        nuevo_celular = Celular(
            modelo=data.get('modelo'),
            anio_fabricacion=data.get('anio_fabricacion'),
            precio=data.get('precio'),
            marca_id=data.get('marca_id')
        )
        try:
            db.session.add(nuevo_celular)
            db.session.commit()
            return CelularSchema().dump(nuevo_celular)
        except IntegrityError:
            db.session.rollback()
            return jsonify({"Error": "No se pudo crear el celular. Verifica que la marca exista y prueba nuevamente."}), 400

    celulares = Celular.query.all()
    return CelularSchema().dump(celulares, many=True)