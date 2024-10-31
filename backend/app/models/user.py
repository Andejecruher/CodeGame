from app.extensions import db
from datetime import datetime
from passlib.context import CryptContext

# Configuración de passlib para hashear contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(db.Model):
    """
    Modelo de usuario para la base de datos.
    """

    __tablename__ = "users"
    id = db.Column(db.String(6), primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password, id):
        """
        Inicializa un nuevo usuario.

        :param email: Dirección de correo electrónico del usuario.
        :param password: Contraseña del usuario (sin hashear).
        :param id: ID único del usuario.
        """
        self.email = email
        self.password = pwd_context.hash(password)  # Hashea la contraseña
        self.id = id

    def check_password(self, password):
        """
        Verifica si la contraseña proporcionada coincide con la almacenada.

        :param password: Contraseña a verificar.
        :return: True si la contraseña coincide, False en caso contrario.
        """
        return pwd_context.verify(password, self.password)

    def to_dict(self):
        return {"id": self.id, "email": self.email}
