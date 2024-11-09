📱 EFI - PYTHON
Este proyecto tiene como objetivo desarrollar una API para gestionar un local de venta de celulares. La API permite realizar las siguientes funcionalidades:

Autenticación y autorización: Login y creación de usuarios.
Gestión de recursos: Endpoints para obtener objetos de todos los modelos (sin restricciones).
Control de acceso: Endpoint para crear nuevos objetos, limitado a usuarios administradores.
Documentación: Endpoints documentados.
Relaciones anidadas: Al menos un modelo contiene otro modelo anidado.
La implementación utiliza Marshmallow para la serialización y validación de datos.

🛠️ Tecnologías Utilizadas
Python: Lenguaje de programación principal.
Flask: Framework ligero para desarrollar aplicaciones web.
Flask-SQLAlchemy: ORM para interactuar con la base de datos usando objetos Python.
Flask-Migrate: Herramienta para gestionar migraciones de bases de datos.
Flask-CORS: Extensión para manejar solicitudes de diferentes orígenes (CORS).
Flask-JWT-Extended: Implementación de autenticación y autorización con JSON Web Tokens (JWT).
Flask-Marshmallow: Serialización y validación de datos.
Werkzeug: Utilidad para manejar datos sensibles como hashes de contraseñas.
dotenv: Carga variables de entorno desde un archivo .env.

🚀 Instalación
Sigue los pasos a continuación para configurar y ejecutar el proyecto localmente:

1. Clonar el repositorio
git clone git@github.com:MatiJFernandez/EFI-Python-Flask.git
cd EFI-Python-Flask
2. Crear un entorno virtual
python3 -m venv entorno
source entorno/bin/activate  # En Windows: entorno\Scripts\activate
3. Instalar dependencias
pip install -r requirements.txt
4. Configurar la base de datos
Iniciar el servidor de base de datos:


sudo /opt/lampp/lampp start
Inicializar y gestionar las migraciones:


flask db init        # Solo la primera vez
flask db migrate -m "Descripción de la migración"  # Detecta cambios en los modelos
flask db upgrade     # Aplica los cambios a la base de datos
5. Ejecutar la aplicación

flask run
Para recargar automáticamente la aplicación tras realizar cambios:
flask run --reload

📚 Funcionalidades Principales
Usuarios y Roles: Control de acceso con roles específicos (administradores y usuarios regulares).
Serialización y Validación: Uso de Marshmallow para validar y formatear datos JSON.
JWT: Autenticación mediante JSON Web Tokens para proteger los endpoints.
Migraciones: Administración de cambios estructurales en la base de datos usando Flask-Migrate.

📄 Documentación de la API
La documentación está disponible directamente en la aplicación. Accede a la documentación de los endpoints en /docs (o un endpoint equivalente).


Autor
Fernández Matías
GitHub



