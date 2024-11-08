from flask import ( 
    Flask, 
    flash, 
    jsonify, 
    redirect, 
    render_template, 
    request, 
    url_for, 
)

import os
from datetime import timedelta
from flask_cors import CORS

from werkzeug.security import (
    generate_password_hash, 
    check_password_hash,
)

from flask_jwt_extended import (
    JWTManager,
    create_access_token, 
    get_jwt,
    get_jwt_identity,
    jwt_required,
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__) 
CORS(app)
#Configuracion
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_ENABLED'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY') or 'tu_clave_secreta'  # Usa una clave secreta segura y constante
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)  # Ajusta la expiración según tus necesidades


# Inicializa las extenciones
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
jwt = JWTManager(app)

from views import register_blueprint 

# Registro de blueprints
register_blueprint(app)

@app.route("/")
def index():
    return render_template('index.html')
