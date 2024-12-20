from app import db

class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    anio_fabricacion = db.Column(db.Integer)
    precio = db.Column(db.Integer)

    #Pertenecer a
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    
    #Relacion directa con el otro objeto
    marca = db.relationship('Marca', backref=db.backref('vehiculos', lazy=True))

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    #modelo = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
    def __str__(self):
        return self.nombre


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean(0), default=False)
    #rol = db.Column(db.String(50), nullable=False)
    #mail = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return dict(
            id= self.id,
            username= self.username,
            password= self.password_hash
        )
    