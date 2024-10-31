from app.extensions import db
from datetime import datetime
import datetime


class Task(db.Model):
    """
    Modelo de tarea para la base de datos.
    """

    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(6), db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(
        db.Enum("Por hacer", "En Curso", "Finalizado"), default="Por hacer"
    )

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
        self.date = date if date else datetime.datetime.now()

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
            "status": self.status,
        }
