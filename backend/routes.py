from flask import request, jsonify
from app import app, db
from models import User, Task
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from passlib.context import CryptContext

# Configuración de passlib para hashear contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.route('/register', methods=['POST'])
def register():
    """
    Registra un nuevo usuario.
    
    Endpoint: /register
    Método: POST
    Datos de entrada (JSON):
        - email: Dirección de correo electrónico del usuario.
        - password: Contraseña del usuario.
    
    Retorna:
        - Un token de acceso JWT si el registro es exitoso.
        - Código de estado 200 si el registro es exitoso.
    """
    data = request.get_json()
    hashed_password = pwd_context.hash(data['password'])  # Hashea la contraseña
    new_user = User(email=data['email'], password=hashed_password, id=f'U{str(db.session.query(User).count() + 1).zfill(4)}')
    db.session.add(new_user)
    db.session.commit()
    token = create_access_token(identity=new_user.id)
    return jsonify(access_token=token), 200

@app.route('/login', methods=['POST'])
def login():
    """
    Inicia sesión de un usuario.
    
    Endpoint: /login
    Método: POST
    Datos de entrada (JSON):
        - email: Dirección de correo electrónico del usuario.
        - password: Contraseña del usuario.
    
    Retorna:
        - Un token de acceso JWT si las credenciales son correctas.
        - Código de estado 200 si el inicio de sesión es exitoso.
        - Código de estado 401 si las credenciales son incorrectas.
    """
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password'], pwd_context):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Bad email or password"}), 401

@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_all_tasks():
    """
    Obtiene todas las tareas del usuario autenticado.
    
    Endpoint: /tasks
    Método: GET
    
    Retorna:
        - Una lista de tareas del usuario autenticado.
        - Código de estado 200 si la solicitud es exitosa.
    """
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": task.id, "title": task.title, "status": task.status, "user_id": task.user_id} for task in tasks]), 200

@app.route('/tasks', methods=['POST'])
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
    new_task = Task(title=data['title'], description=data['description'], user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"msg": "Task added"}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
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
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"msg": "Task not found"}), 404
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    db.session.commit()
    return jsonify({"msg": "Task updated"}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
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
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"msg": "Task deleted"}), 200
    return jsonify({"msg": "Task not found"}), 404

@app.route('/', methods=['GET'])
def home():
    """
    Endpoint de prueba para verificar que el servidor está funcionando.
    
    Endpoint: /
    Método: GET
    
    Retorna:
        - Un mensaje de bienvenida.
        - Código de estado 200 si la solicitud es exitosa.
    """
    return jsonify({"msg": "Hello, World !!"}), 200