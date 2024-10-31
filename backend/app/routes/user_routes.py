from flask import Blueprint, request
from app.services.user_services import create_user, access_user

user_routes = Blueprint("users", __name__)


@user_routes.route("/register", methods=["POST"])
def register():
    """
    Endpoint para crear usuario.
    
    ---
    tags:
      - Autenticación
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: "test@gmail.com"
              description: Nombre de usuario del usuario que intenta iniciar sesión.
            password:
              type: string
              example: "secret"
              description: Contraseña del usuario que intenta iniciar sesión.
    responses:
      200:
        description: Respuesta exitosa con token de autenticación.
        schema:
          type: object
          properties:
            token:
              type: string
              example: "123abc"
            user:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                username:
                  type: string
                  example: "user1"
                email:
                  type: string
                  example: "example@gmail.com"
      401:
        description: Credenciales incorrectas.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Credenciales inválidas"
    """
    data = request.get_json()
    return create_user(data)


@user_routes.route("/login", methods=["POST"])
def login():
    """
    Endpoint para iniciar sesión.
    
    ---
    tags:
      - Autenticación
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: "test@gmail.com"
              description: Nombre de usuario del usuario que intenta iniciar sesión.
            password:
              type: string
              example: "secret"
              description: Contraseña del usuario que intenta iniciar sesión.
    responses:
      200:
        description: Respuesta exitosa con token de autenticación.
        schema:
          type: object
          properties:
            token:
              type: string
              example: "123abc"
            user:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                username:
                  type: string
                  example: "user1"
                email:
                  type: string
                  example: "example@gmail.com"
      401:
        description: Credenciales incorrectas.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Credenciales inválidas"
    """
    data = request.get_json()
    return access_user(data)
