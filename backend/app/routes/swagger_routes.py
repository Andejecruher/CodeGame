# routes/swagger_routes.py

from flask import Blueprint, jsonify, current_app
from flask_swagger import swagger

swagger_routes = Blueprint("swagger", __name__)


@swagger_routes.route("/swagger", methods=["GET"])
def swagger_spec():
    # Usar la aplicación Flask actual
    """
    Genera el esquema Swagger para las rutas definidas.

    Endpoint: /swagger
    Método: GET

    Retorna:
        - El esquema Swagger en formato JSON.
    """
    return jsonify(swagger(current_app))  # Pasar la instancia de la aplicación Flask
