from repositories.accesorio_repositories import AccesorioRepositories

class AccesorioService:
    def __init__(self, accesorio_repository: AccesorioRepositories):
        self._accesorio_repository = accesorio_repository

    def get_all(self):
        return self._accesorio_repository.get_all()

    def get_by_id(self, id):
        return self._accesorio_repository.get_by_id(id)

    def create(self, nombre):
        self._accesorio_repository.create(nombre)

    def update(self, id, nombre):
        self._accesorio_repository.update(id, nombre)

    def delete(self, id):
        self._accesorio_repository.delete(id)