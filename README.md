# CodeGame

Prueba técnica para aplicación a vacante en CodeGame

## Requerimientos previos para Backend

- Instala Python y MariaDB:

- Python: Descárgalo de [python.org](https://python.org).
- MariaDB: Descárgalo desde [mariadb.org](https://mariadb.org).
- Node.js: Descárgalo de [nodejs.org](https://nodejs.org). en su versión v21.6.1.
- npm: Se instala automáticamente con Node.js.

# Crear un entorno virtual para Python:

Abre una terminal o línea de comandos y navega a la carpeta donde quieres crear el proyecto.

Has un clon del repositorio con el siguiente comando:

```bash
git clone https://github.com/Andejecruher/CodeGame.git
```
Accede a la carpeta del proyecto:

```bash
cd CodeGame
```

Luego sigue los pasos necesarios para levantar tanto el servicio de backend como el de frontend.


Primero accede a la carpeta del backend:

```bash
cd backend
```
Ejecuta el siguiente comando para crear el entorno virtual:

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

#Instalar dependencias de Python:

- Instalar Flask y Flask-JWT-Extended para el backend con pip install Flask Flask-JWT-Extended Flask-SQLAlchemy pymysql passlib flask-cors

```bash
pip install Flask Flask-JWT-Extended Flask-SQLAlchemy pymysql passlib flask-cors
```

# Crear la base de datos:

- Corre el script de la carpeta DB para crear la base de datos y la tabla necesaria.

```bash
mysql -u root -p < db.sql
```
- Recuerda cambiar los datos de conexión por los tuyos


# Correr el servidor:

- Antes de correr el servidor, asegurate de colocar las credenciales de la base de datos en el archivo config.py

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<usuario>:<contraseña>@localhost/<nombre de la base de datos>'
JWT_SECRET_KEY = 'clave secreta'
```


- instala guicorn con pip install gunicorn

```bash
pip install gunicorn
```

- Corre el servidor con el siguiente comando:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app --reload
```

- Recuerda correr los comandos dentro de la carpeta backend a la altura de el archivo app.py para que funcione correctamente.

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

- Abre [http://localhost:3000](http://localhost:3000) en tu navegador para ver la aplicación.

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
