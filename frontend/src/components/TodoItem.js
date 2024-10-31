// src/components/TodoItem.js
import { format } from 'date-fns';

const TodoItem = ({ task, updateTaskStatus, deleteTask, startEditingTask }) => {
    // Manejar el cambio de estado de la tarea
    const handleStatusChange = (e) => {
        updateTaskStatus(task.id, e.target.value);
    };

    // Estilos dinámicos según el estado
    const statusStyles = {
        "Por hacer": "bg-yellow-100 text-yellow-700",
        "En Curso": "bg-blue-100 text-blue-700",
        "Finalizado": "bg-green-100 text-green-700",
    };

    // Formatear la fecha
    const formattedDate = format(task.date, 'dd/MM/yyyy hh:mm');

    return (
        <div className="p-4 mb-4 bg-white rounded-lg shadow-md flex flex-col justify-between items-start space-y-4">
            <div className="flex-1 w-full">
                <h3 className="text-lg font-semibold text-gray-800">{task.title}</h3>
                <p className="text-gray-600">{task.description}</p>
                <p className="text-sm text-gray-500 mt-2">Fecha: {formattedDate}</p>
            </div>
            <div className="flex flex-col items-start space-y-2 w-full">
                <select
                    value={task.status}
                    onChange={handleStatusChange}
                    className={`w-full p-2 text-sm border rounded-lg ${statusStyles[task.status]}`}
                >
                    <option value="Por hacer">Por hacer</option>
                    <option value="En Curso">En curso</option>
                    <option value="Finalizado">Finalizado</option>
                </select>
                <button 
                    onClick={() => startEditingTask(task)} 
                    className="w-full px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors text-sm"
                >
                    Editar
                </button>
                <button 
                    onClick={() => deleteTask(task.id)} 
                    className="w-full px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition-colors text-sm"
                >
                    Eliminar
                </button>
            </div>
        </div>
    );
};

export default TodoItem;
