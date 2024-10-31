# Backend

## Descripción
Api para Todo list de tareas y control de usuarios.

## Requisitos
- Python 3.x
- MariaDB
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- PyMySQL
- Passlib
- Flask-Cors
- Gunicorn

## Instalación de Backend
1. Clona el repositorio:
  ```bash
  git clone https://github.com/Andejecruher/CodeGame.git
  ```
2. Navega al directorio del proyecto:
  ```bash
  cd CodeGame/backend
  ```
3. Ejecuta el siguiente comando para crear el entorno virtual:

  ```bash
  python -m venv todo_env
  ```

  Activa el entorno virtual:

  - En Windows: 
  ```bash
  todo_env\Scripts\activate
  ```
  - En Mac o Linux: 
  
  ```bash
  source todo_env/bin/activate
  ```
4. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```
5. Configura las variables de entorno:
  ```bash
  cp .env.example .env
  ```
  - Cambia los valores de las variables de entorno por los tuyos
  
6. crea la base de datos:
  ```bash
  mysql -u root -p < db.sql
  ```
  - Recuerda cambiar los datos de conexión por los tuyos
  
7. Corre el servidor:
  ```bash
  flask run
  ```

[Enlace al proyecto en GitHub](https://github.com/Andejecruher/CodeGame)