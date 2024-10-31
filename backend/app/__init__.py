# Importar las librerías necesarias
from flask import Flask, jsonify  # Framework para crear aplicaciones web
from flask_cors import (
    CORS,
)  # Configurar CORS para permitir solicitudes desde localhost:3000
from flask_swagger_ui import get_swaggerui_blueprint # Importar Swagger UI
from app.config import Config  # Configuración de la aplicación
from app.routes import register_blueprints  # Importar las rutas de la aplicación
from app.extensions import db, jwt  # Importar las extensiones de la aplicación


def create_app():

    # Crear la aplicación Flask
    app = Flask(__name__)
    # Configurar la aplicación usando la configuración del objeto Config
    app.config.from_object(Config)
    # Configura CORS para permitir solicitudes desde localhost:3000
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    # Inicializar la base de datos
    try:
        db.init_app(app)
    except Exception as e:
        # Manejar errores de inicialización de la base de datos
        print(f"Error al inicializar la base de datos: {e}")
    # Inicializar JWT
    try:
        jwt.init_app(app)
    except Exception as e:
        # Manejar errores de inicialización de JWT
        print(f"Error al inicializar JWT: {e}")
    # Registrar las rutas de la aplicación
    register_blueprints(app)
    # Configuración de Swagger UI
    SWAGGER_URL = '/swagger-ui'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL,
        config={'app_name': "Documentacion de la API"}
    )    

    # Registrar el Blueprint de Swagger UI
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
