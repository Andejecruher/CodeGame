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

    ---
    tags:
      - Tareas
    parameters:
      - name: Authorization
        in: header
        required: true
        type: string
        description: "Token de autenticación (Bearer <token>)"
    responses:
      200:
        description: Lista de tareas del usuario autenticado.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              title:
                type: string
                example: "Tarea de ejemplo"
              description:
                type: string
                example: "Descripción de la tarea"
              status:
                type: string
                example: "pendiente"
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

    ---
    tags:
      - Tareas
    parameters:
      - name: Authorization
        in: header
        required: true
        type: string
        description: "Token de autenticación (Bearer <token>)"
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Nueva tarea"
              description: "Título de la tarea"
            description:
              type: string
              example: "Descripción de la nueva tarea"
              description: "Descripción de la tarea"
    responses:
      201:
        description: Tarea agregada exitosamente.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Tarea creada con éxito"
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

    ---
    tags:
      - Tareas
    parameters:
      - name: Authorization
        in: header
        required: true
        type: string
        description: "Token de autenticación (Bearer <token>)"
      - name: task_id
        in: path
        required: true
        type: integer
        description: ID de la tarea a actualizar.
      - name: body
        in: body
        required: false
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Título actualizado"
            description:
              type: string
              example: "Descripción actualizada"
            status:
              type: string
              example: "Por hacer"
    responses:
      200:
        description: Tarea actualizada exitosamente.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Tarea actualizada con éxito"
      404:
        description: Tarea no encontrada.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Tarea no encontrada"
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

    ---
    tags:
      - Tareas
    parameters:
      - name: Authorization
        in: header
        required: true
        type: string
        description: "Token de autenticación (Bearer <token>)"
      - name: task_id
        in: path
        required: true
        type: integer
        description: ID de la tarea a eliminar.
    responses:
      200:
        description: Tarea eliminada exitosamente.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Tarea eliminada con éxito"
      404:
        description: Tarea no encontrada.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Tarea no encontrada"
    """
    user_id = get_jwt_identity()
    return delete_task(user_id, task_id)
