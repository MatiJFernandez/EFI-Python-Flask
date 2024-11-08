from repositories.accesorio_repositories import AccesorioRepositories

class AccesorioService:
    def __init__(self):
        self.repository = AccesorioRepositories()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def create(self, nombre):
        self.repository.create(nombre)

    def update(self, id, nombre):
        self.repository.update(id, nombre)

    def delete(self, id):
        self.repository.delete(id)