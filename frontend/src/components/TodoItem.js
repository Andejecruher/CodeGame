// src/components/TodoItem.js
import { format } from 'date-fns';

const TodoItem = ({ task, updateTaskStatus, deleteTask, startEditingTask }) => {
    const handleStatusChange = (e) => {
        updateTaskStatus(task.id, e.target.value);
    };

    // Estilos dinámicos según el estado
    const statusStyles = {
        "Por hacer": "bg-yellow-100 text-yellow-700",
        "En Curso": "bg-blue-100 text-blue-700",
        "Finalizado": "bg-green-100 text-green-700",
    };

    const formattedDate = format(task.date, 'dd/MM/yyyy HH:mm');

    return (
        <div className="p-4 mb-4 bg-gray-100 rounded-lg shadow-md flex flex-col sm:flex-row justify-between items-start sm:items-center">
            <div>
                <h3 className="text-lg font-bold">{task.title}</h3>
                <p>{task.description}</p>
                <p className="text-sm text-gray-600">Fecha: {formattedDate}</p>
            </div>
            <div className="flex flex-col sm:flex-row sm:items-center mt-2 sm:mt-0">
                <select
                    value={task.status}
                    onChange={handleStatusChange}
                    className={`p-2 border rounded mb-2 sm:mb-0 sm:mr-2 ${statusStyles[task.status]}`}
                >
                    <option value="Por hacer">Por hacer</option>
                    <option value="En Curso">En curso</option>
                    <option value="Finalizado">Finalizado</option>
                </select>
                <button 
                    onClick={() => startEditingTask(task)} 
                    className="ml-2 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
                >
                    Editar
                </button>
                <button 
                    onClick={() => deleteTask(task.id)} 
                    className="ml-2 bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                >
                    Eliminar
                </button>
            </div>
        </div>
    );
};

export default TodoItem;
