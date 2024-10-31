import sys
import os
import pytest

# Añadir el directorio 'backend' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db

@pytest.fixture(scope='module')
def test_client():
    # Crear la app en modo de pruebas
    flask_app = create_app()  # Configura la app para pruebas

    # Crear un contexto de aplicación
    with flask_app.app_context():
        # Crear todas las tablas en la base de datos de pruebas
        db.create_all()

        # Crear y devolver un cliente de pruebas
        testing_client = flask_app.test_client()
        yield testing_client  # Cliente que se usará en los tests

        # Eliminar todas las tablas después de los tests
        db.drop_all()