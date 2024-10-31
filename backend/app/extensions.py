from flask_sqlalchemy import SQLAlchemy  # ORM Para las consultas a la base de datos
from flask_jwt_extended import JWTManager  # JWT para autenticación

db = SQLAlchemy()
jwt = JWTManager()
