// src/components/TaskForm.js
import { useState, useEffect } from 'react';

const TaskForm = ({ addTask, updateTask, editingTask, setEditingTask }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    // Si se está editando una tarea, se cargan los datos en el formulario
    useEffect(() => {
        if (editingTask) {
            setTitle(editingTask.title);
            setDescription(editingTask.description);
        }
    }, [editingTask]);

    // Función para manejar el envío del formulario
    const handleSubmit = (e) => {
        e.preventDefault();
        const taskData = { title, description };
        if (editingTask) {
            updateTask(editingTask.id, taskData);
            setEditingTask(null);
        } else {
            addTask(taskData);
        }
        setTitle('');
        setDescription('');
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 mb-4 bg-white rounded shadow-md">
            <h3 className="text-lg font-bold mb-2">{editingTask ? 'Editar Tarea' : 'Agregar Tarea'}</h3>
            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="title">
                    Título
                </label>
                <input
                    id="title"
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    required
                />
            </div>
            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="description">
                    Descripción
                </label>
                <textarea
                    id="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    required
                />
            </div>
            <div className="flex items-center justify-between">
                <button
                    type="submit"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    {editingTask ? 'Actualizar Tarea' : 'Agregar Tarea'}
                </button>
                {editingTask && (
                    <button
                        type="button"
                        onClick={() => setEditingTask(null)}
                        className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    >
                        Cancelar
                    </button>
                )}
            </div>
        </form>
    );
};

export default TaskForm;