-- Crear la base de datos
CREATE DATABASE todo_app;
USE todo_app;

-- Crear la tabla de usuarios
CREATE TABLE users (
    id VARCHAR(6) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Crear la tabla de tareas
CREATE TABLE tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id VARCHAR(6),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    status ENUM('Por hacer', 'En Curso', 'Finalizado') DEFAULT 'Por hacer',
    FOREIGN KEY (user_id) REFERENCES users(id)
);

