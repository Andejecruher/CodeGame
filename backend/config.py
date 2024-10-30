class Config:
    """
    Configuración para la aplicación.

    Atributos:
        SQLALCHEMY_DATABASE_URI (str): URI de la base de datos para SQLAlchemy.
        JWT_SECRET_KEY (str): Clave secreta para la generación de JWT.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Desactiva el seguimiento de modificaciones de objetos para ahorrar memoria.
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:secret@localhost/todo_app'
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
