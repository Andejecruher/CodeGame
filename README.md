# CodeGame

Prueba técnica para aplicación a vacante en CodeGame

## Requerimientos previos para Backend

- Instala Python y MariaDB:

- Python: Descárgalo de [python.org](https://python.org).
- MariaDB: Descárgalo desde [mariadb.org](https://mariadb.org).

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


- Abre [http://localhost:5000](http://localhost:5000) en tu navegador para ver la aplicación o visualiza el puerto asignado por tu servidor en la terminal.
- Listo, ya puedes empezar a usar la aplicación.
- Para detener el servidor, presiona `Ctrl + C` en la terminal.
  
# Documentacion oficial:

- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/)
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/)
- [Passlib](https://passlib.readthedocs.io/en/stable/)
- [Gunicorn](https://gunicorn.org/)
- [MariaDB](https://mariadb.org/)


## Requerimientos previos para Frontend

- Instala Node.js y npm en su version v21.6.1.

# Correr el servidor de desarrollo para el frontend:

- Dentro de la carpeta del proyecto, accede a la carpeta frontend:

```bash 
cd frontend
```

- Instala las dependencias con el siguiente comando:

```bash
npm install
```

- Corre el servidor de desarrollo con el siguiente comando:

```bash
npm run dev
```

- Abre [http://localhost:3000](http://localhost:3000) en tu navegador para ver la aplicación o verifica el puerto asignado por tu servidor en la terminal.

- Listo, ya puedes empezar a usar la aplicación.

## Estructura del Proyecto

El proyecto se divide en dos carpetas principales: backend y frontend. La estructura de carpetas es la siguiente:

```
CodeGame/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── db.sql
│   ├── __init__.py
│   └── todo_env/
│       ├── bin/
│       ├── include/
│       ├── lib/
│       ├── lib64 -> lib
│       ├── pyvenv.cfg
│       └── share/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Alert.js
│   │   │   ├── TaskForm.js
│   │   │   └── TodoItem.js
│   │   ├── context/
│   │   │   └── AuthContext.js
│   │   ├── pages/
|   |   |   ├── auth
│   │   │   │   ├── Login.js
│   │   │   │   └── Register.js
│   │   │   └── _app.js
│   │   │   ├── dashboard.js
│   │   │   ├── styles
│   │   │   │   ├── Auth.module.css
│   │   │   │   ├── globals.css
│   │   └── utils/
│   │       └── api.js
│   ├── public/
│   ├── styles/
│   ├── .env.local
│   ├── .gitignore
│   ├── next.config.js
│   ├── package.json
│   └── yarn.lock
├── .gitignore
└── README.md
```
[Enlace al proyecto en GitHub](https://github.com/Andejecruher/CodeGame)