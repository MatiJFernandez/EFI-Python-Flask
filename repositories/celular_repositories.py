from app import db
from models import Celular

class CelularRepositories:
    def get_all(self):
        return Celular.query.all()
    
    def get_by_id(self, id):
        return Celular.query.get_or_404(id)

    def create(self, modelo, anio_fabricacion, precio, marca):
        nuevo_celular = Celular(modelo=modelo, anio_fabricacion=anio_fabricacion, precio=precio, marca_id=marca)
        db.session.add(nuevo_celular)
        db.session.commit()
        return nuevo_celular
    
    def update(self, id, nombre):
        accesorio = self.get_by_id(id)
        accesorio.nombre = nombre
        db.session.commit()

    def delete(self, id):
        accesorio = self.get_by_id(id)
        db.session.delete(accesorio)
        db.session.commit()