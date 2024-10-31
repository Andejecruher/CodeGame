import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


class Config:
    """
    Configuración para la aplicación.

    Atributos:
        SQLALCHEMY_DATABASE_URI (str): URI de la base de datos para SQLAlchemy.
        JWT_SECRET_KEY (str): Clave secreta para la generación de JWT.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Desactiva el seguimiento de modificaciones de objetos para ahorrar memoria.
    """

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost/{os.getenv('DB_NAME')}"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
