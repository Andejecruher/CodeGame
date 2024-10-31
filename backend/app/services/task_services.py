from flask import jsonify
from app.models.task import Task
from app.extensions import db
import datetime


def get_tasks(user_id):
    """
    Obtiene todas las tareas del usuario autenticado.

    Retorna:
        - Una lista de tareas.
    """
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks]), 200


def create_task(data, user_id):
    """
    Agrega una nueva tarea para el usuario autenticado.

    Datos de entrada:
        - title: Título de la tarea.
        - description: Descripción de la tarea.

    Retorna:
        - Un mensaje de confirmación.
    """
    new_task = Task(
        title=data["title"], description=data["description"], user_id=user_id
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"msg": "Task added"}), 201


def update_task(data, user_id, task_id):
    """
    Actualiza una tarea existente del usuario autenticado.

    Datos de entrada:
        - title: Nuevo título de la tarea (opcional).
        - description: Nueva descripción de la tarea (opcional).
        - status: Nuevo estado de la tarea (opcional).

    Retorna:
        - Un mensaje de confirmación.
    """
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if task:
        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "status" in data:
            if data["status"] != task.status:
                task.date = datetime.datetime.now()
            task.status = data["status"]
        db.session.commit()
        return jsonify({"msg": "Task updated"}), 200
    else:
        return jsonify({"msg": "Task not found"}), 404


def delete_task(user_id, task_id):
    """
    Elimina una tarea existente del usuario autenticado.

    Retorna:
        - Un mensaje de confirmación.
    """
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"msg": "Task deleted"}), 200
    else:
        return jsonify({"msg": "Task not found"}), 404
