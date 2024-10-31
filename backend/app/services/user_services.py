from flask import jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.extensions import db


def create_user(data):
    """
    Registra un nuevo usuario.

    Datos de entrada:
        - email: Dirección de correo electrónico del usuario.
        - password: Contraseña del usuario.

    Retorna:
        - Un mensaje de confirmación.
    """
    new_user = User(email=data["email"], password=data["password"], id=f'U{str(db.session.query(User).count() + 1).zfill(4)}')
    db.session.add(new_user)
    db.session.commit()
    token = create_access_token(identity=new_user.id)
    return jsonify({"access_token": token, "user": new_user.to_dict()}), 200


def access_user(data):
    """
    Inicia sesión de un usuario.

    Datos de entrada:
        - email: Dirección de correo electrónico del usuario.
        - password: Contraseña del usuario.

    Retorna:
        - Un mensaje de confirmación.
    """
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"access_token": token, "user": user.to_dict()}), 200
    return jsonify({"msg": "Bad email or password"}), 401
