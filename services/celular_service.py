from app import db
from repositories.celular_repositories import CelularRepositories
from models import Celular

class CelularService:
    def __init__(self, celular_repository: CelularRepositories):
        self._celular_repository = celular_repository

    def get_all(self):
        return self._celular_repository.get_all()
    
    def get_by_id(self, id):
        return self._celular_repository.get_by_id(id)

    def create(self, modelo, anio_fabricacion, precio, marca):
        return self._celular_repository.create(modelo, anio_fabricacion, precio, marca)

    def delete_with_accesorios(self, id):
        celular = self._celular_repository.get_by_id(id)
        
        for accesorio in celular.accesorios:
            db.session.delete(accesorio)
        
        db.session.delete(celular)
        db.session.commit()

    def get_accesorios_by_celular(self, celular_id):
        return self._celular_repository.get_accesorios_by_celular(celular_id)

