
from .auth_views import auth_bp
from .celulares_view import celular_bp
from .marca_view import marca_bp


def register_blueprint (app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(celular_bp)
    app.register_blueprint(marca_bp)  

    