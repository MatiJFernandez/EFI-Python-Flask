from app import ma
from marshmallow import validates, ValidationError
from models import User, Marca, Celular, Accesorio


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password_hash = ma.auto_field()
    is_admin = ma.auto_field()

class UserMinimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()


class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca

    id=ma.auto_field()
    nombre=ma.auto_field()

class CelularSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Celular

    id = ma.auto_field()
    modelo = ma.auto_field()
    anio_fabricacion = ma.auto_field()
    precio = ma.auto_field()
    marca_id = ma.auto_field()
    marca_id = ma.auto_field()
    marca = ma.Nested(MarcaSchema)
    marca = ma.Nested(MarcaSchema)

class AccesorioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Accesorio

    id=ma.auto_field()
    nombre=ma.auto_field()
    