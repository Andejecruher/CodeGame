from flask import Blueprint, request
from app.services.user_services import create_user, access_user

user_routes = Blueprint("users", __name__)


@user_routes.route("/register", methods=["POST"])
def register():
    """
    Registra un nuevo usuario.

    Endpoint: /register
    Método: POST
    Datos de entrada (JSON):
        - email: Dirección de correo electrónico del usuario.
        - password: Contraseña del usuario.

    Retorna:
        - Un token de acceso JWT si el registro es exitoso.
        - Código de estado 200 si el registro es exitoso.
    """
    data = request.get_json()
    return create_user(data)


@user_routes.route("/login", methods=["POST"])
def login():
    """
    Inicia sesión de un usuario.

    Endpoint: /login
    Método: POST
    Datos de entrada (JSON):
        - email: Dirección de correo electrónico del usuario.
        - password: Contraseña del usuario.

    Retorna:
        - Un token de acceso JWT si las credenciales son correctas.
        - Código de estado 200 si el inicio de sesión es exitoso.
        - Código de estado 401 si las credenciales son incorrectas.
    """
    data = request.get_json()
    return access_user(data)
