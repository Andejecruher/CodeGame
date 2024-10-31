# tests/test_user_routes.py
import json
import pytest

@pytest.mark.run(order=1)
def test_register(test_client):
    """
    Prueba para el endpoint de registro de usuario.
    """
    response = test_client.post('/register', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'access_token' in data
    assert 'user' in data

@pytest.mark.run(order=2)
def test_login(test_client):
    """
    Prueba para el endpoint de inicio de sesión.
    """
    # Luego, iniciar sesión con el usuario registrado
    response = test_client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'access_token' in data
    assert 'user' in data