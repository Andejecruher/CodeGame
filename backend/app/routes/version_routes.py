from flask import Blueprint, redirect

version_routes = Blueprint("version", __name__)


@version_routes.route("/version", methods=["GET"])
def home():
    """
    Endpoint de prueba para verificar que el servidor está funcionando.

    Endpoint: /version
    Método: GET

    Retorna:
        - Un mensaje de bienvenida.
        - Código de estado 200 si la solicitud es exitosa.
    """
    return "Version 0.01", 200


@version_routes.route("/")
def home_redirect():
    """
    Endpoint de prueba para verificar que el servidor está funcionando.

    Endpoint: /version
    Método: GET

    Retorna:
        - Un mensaje de bienvenida.
        - Código de estado 200 si la solicitud es exitosa.
    """
    return redirect("/version")
