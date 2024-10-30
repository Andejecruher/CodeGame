# Importar las librerías necesarias
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la aplicación usando la configuración del objeto Config
app.config.from_object(Config)

# Inicializar la base de datos
try:
    db = SQLAlchemy(app)
except Exception as e:
    # Manejar errores de inicialización de la base de datos
    print(f"Error al inicializar la base de datos: {e}")

# Inicializar JWT
try:
    jwt = JWTManager(app)
except Exception as e:
    # Manejar errores de inicialización de JWT
    print(f"Error al inicializar JWT: {e}")

# Importar las rutas de la aplicación
from routes import *

# Ejecutar la aplicación solo si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
