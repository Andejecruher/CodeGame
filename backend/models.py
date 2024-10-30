import datetime
from app import db
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


class Task(db.Model):
    """
    Modelo de tarea para la base de datos.
    """
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(6), db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum("Por hacer", "En Curso", "Finalizado"), default="Por hacer")

    def __init__(self, user_id, title, description, status="Por hacer", date=None):
        """
        Inicializa una nueva tarea.
        
        :param user_id: ID del usuario al que pertenece la tarea.
        :param title: Título de la tarea.
        :param description: Descripción de la tarea.
        :param status: Estado de la tarea (por defecto "Por hacer").
        :param date: Fecha y hora de la tarea (por defecto la fecha y hora actual).
        """
        self.user_id = user_id
        self.title = title
        self.description = description
        self.status = status
        self.date = date if date else datetime.datetime.utcnow()

    def to_dict(self):
        """
        Convierte el objeto Task a un diccionario.
        
        :return: Diccionario con los datos de la tarea.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "date": self.date.isoformat(),
            "description": self.description,
            "status": self.status
        }