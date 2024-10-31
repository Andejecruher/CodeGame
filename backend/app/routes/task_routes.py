from flask import Blueprint, request, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.task_services import create_task, get_tasks, update_task, delete_task

task_routes = Blueprint("tasks", __name__)


@task_routes.route("/tasks", methods=["GET"])
@jwt_required()
def list_tasks():
    """
    Obtiene todas las tareas del usuario autenticado.

    Endpoint: /tasks
    Método: GET

    Retorna:
        - Una lista de tareas del usuario autenticado.
        - Código de estado 200 si la solicitud es exitosa.
    """
    user_id = get_jwt_identity()
    tasks = get_tasks(user_id)
    return tasks


@task_routes.route("/tasks", methods=["POST"])
@jwt_required()
def add_task():
    """
    Agrega una nueva tarea para el usuario autenticado.

    Endpoint: /tasks
    Método: POST
    Datos de entrada (JSON):
        - title: Título de la tarea.
        - description: Descripción de la tarea.

    Retorna:
        - Un mensaje de confirmación.
        - Código de estado 201 si la tarea se agrega exitosamente.
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    return create_task(data, user_id)


@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def edit_task(task_id):
    """
    Actualiza una tarea existente del usuario autenticado.

    Endpoint: /tasks/<int:task_id>
    Método: PUT
    Datos de entrada (JSON):
        - title: Nuevo título de la tarea (opcional).
        - description: Nueva descripción de la tarea (opcional).
        - status: Nuevo estado de la tarea (opcional).

    Retorna:
        - Un mensaje de confirmación.
        - Código de estado 200 si la tarea se actualiza exitosamente.
        - Código de estado 404 si la tarea no se encuentra.
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    return update_task(data, user_id, task_id)


@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def remove_task(task_id):
    """
    Elimina una tarea existente del usuario autenticado.

    Endpoint: /tasks/<int:task_id>
    Método: DELETE

    Retorna:
        - Un mensaje de confirmación.
        - Código de estado 200 si la tarea se elimina exitosamente.
        - Código de estado 404 si la tarea no se encuentra.
    """
    user_id = get_jwt_identity()
    return delete_task(user_id, task_id)


@task_routes.route("/version", methods=["GET"])
def home():
    """
    Endpoint de prueba para verificar que el servidor está funcionando.

    Endpoint: /version
    Método: GET

    Retorna:
        - Un mensaje de bienvenida.
        - Código de estado 200 si la solicitud es exitosa.
    """
    return "Version 0.01", 200


@task_routes.route("/")
def home_redirect():
    """
    Endpoint de prueba para verificar que el servidor está funcionando.

    Endpoint: /version
    Método: GET

    Retorna:
        - Un mensaje de bienvenida.
        - Código de estado 200 si la solicitud es exitosa.
    """
    return redirect("/version")
