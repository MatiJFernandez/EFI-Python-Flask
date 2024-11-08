from app import db
from models import Marca

class MarcaRepositories:
    def get_all(self):
        return Marca.query.all()

    def create(self, nombre):
        nueva_marca = Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return nueva_marca

    def get_by_id(self, id):
        return Marca.query.get_or_404(id)

    def update(self, marca):
        marca.nombre = "Nueva marca"
        db.session.commit()

    def get_celulares_por_marca(self, marca_id):
        marca = self.get_by_id(marca_id)
        return marca.celulares  
    