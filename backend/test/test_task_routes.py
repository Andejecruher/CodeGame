# tests/test_task_routes.py
import json

def test_list_tasks(test_client):
    """
    Prueba para el endpoint de listar tareas.
    """
    # Primero, registrar e iniciar sesión con un usuario
    test_client.post('/register', json={
        'email': 'testtask@example.com',
        'password': 'password123'
    })
    login_response = test_client.post('/login', json={
        'email': 'testtask@example.com',
        'password': 'password123'
    })
    token = json.loads(login_response.data)['access_token']

    # Luego, listar las tareas del usuario autenticado
    response = test_client.get('/tasks', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200

def test_create_task(test_client):
    """
    Prueba para el endpoint de crear tarea.
    """
    # Primero, registrar e iniciar sesión con un usuario
    test_client.post('/register', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    login_response = test_client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    token = json.loads(login_response.data)['access_token']

    # Luego, crear una tarea para el usuario autenticado
    response = test_client.post('/tasks', json={
        'title': 'Nueva Tarea',
        'description': 'Descripción de la nueva tarea'
    }, headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 201