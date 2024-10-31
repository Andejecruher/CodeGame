from flask import Blueprint, redirect

version_routes = Blueprint("version", __name__)


@version_routes.route("/version", methods=["GET"])
def home():
    """
    Endpoint de prueba para verificar que el servidor está funcionando.

    Endpoint: /version
    Método: GET

    ---
    tags:
      - Versión
    responses:
      200:
        description: Mensaje de bienvenida.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Version 0.01"
    """
    return "Version 0.01", 200


@version_routes.route("/", methods=["GET"])
def home_redirect():
    """
    Redirige a la versión de la API.

    Endpoint: /
    Método: GET
    """
    return redirect("/version")
