// pages/dashboard.js
import { useAuth } from '../context/AuthContext';
import TaskForm from '../components/TaskForm';
import TodoItem from '../components/TodoItem';
import { useEffect, useState } from 'react';
import { getTasks, addTask as addTaskApi, updateTask as updateTaskApi, deleteTask as deleteTaskApi } from '../utils/api';

const Dashboard = () => {
    const { user, logout, token } = useAuth();
    const [tasks, setTasks] = useState([
        { id: 1, title: "Tarea 1", description: "Descripción de tarea 1", status: "Por hacer", date: "2024-10-30" },
        { id: 2, title: "Tarea 2", description: "Descripción de tarea 2", status: "En curso", date: "2024-10-31" },
    ]);
    const [editingTask, setEditingTask] = useState(null); // Para almacenar la tarea en edición
    const [loading, setLoading] = useState(true);

    const fetchTasks = async () => {
        try {
            const fetchedTasks = await getTasks(token);
            setTasks(fetchedTasks);
        } catch (error) {
            setError('Failed to fetch tasks');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchTasks();
    }, [token]);

    const addTask = async (newTask) => {
        try {
            const addedTask = await addTaskApi(token, newTask.title, newTask.description, newTask.date);
            setTasks([...tasks, addedTask]);
            fetchTasks();
        } catch (error) {
            setError('Failed to add task');
        }
    };


    const updateTask = async (id, updatedTask) => {
        try {
            const updatedTaskData = await updateTaskApi(token, id, updatedTask.title, updatedTask.description);
            setTasks(tasks.map(task => task.id === id ? updatedTaskData : task));
            fetchTasks();
        } catch (error) {
            setError('Failed to update task');
        }
    };

    const updateTaskStatus = async (id, newStatus) => {
        try {
            const taskToUpdate = tasks.find(task => task.id === id);
            const updatedTask = await updateTaskApi(token, id, taskToUpdate.title, taskToUpdate.description, newStatus);
            setTasks(tasks.map(task => task.id === id ? updatedTask : task));
            fetchTasks();
        } catch (error) {
            setError('Failed to update task');
        }
    };

    const deleteTask = async (id) => {
        try {
            await deleteTaskApi(token, id);
            setTasks(tasks.filter(task => task.id !== id));
            fetchTasks();
        } catch (error) {
            setError('Failed to delete task');
        }
    };

    const startEditingTask = (task) => {
        setEditingTask(task);
    };
    // Filtrar tareas por estado
    const tasksToDo = tasks.length > 0 ? tasks.filter(task => task.status === "Por hacer") : [];
    const tasksInProgress = tasks.length > 0 ? tasks.filter(task => task.status === "En Curso") : [];
    const tasksDone = tasks.length > 0 ? tasks.filter(task => task.status === "Finalizado") : [];

    return (
        <div className="min-h-screen bg-gray-100 flex flex-col items-center">
            <header className="bg-blue-600 w-full py-4 flex justify-between items-center px-6 text-white">
                <div>
                    <h1 className="text-2xl font-bold">Bienvenido !</h1>
                    <p>{user?.email}</p>
                </div>
                <button onClick={logout} className="bg-red-500 px-4 py-2 rounded">Logout</button>
            </header>

            <main className="w-full max-w-3xl p-4 mt-6">

                <div className="text-center mb-6">
                    <h1 className="text-4xl font-bold text-blue-600">CodeGame Task</h1>
                </div>

                {/* Formulario de creación */}
                {editingTask === null && <TaskForm addTask={addTask} updateTask={updateTask} editingTask={editingTask} setEditingTask={setEditingTask} />}

                {/* Formulario de edición */}
                {editingTask && (
                    <TaskForm addTask={addTask} updateTask={updateTask} editingTask={editingTask} setEditingTask={setEditingTask} />
                )}

                <h2 className="text-2xl font-semibold mb-4">Lista de Tareas</h2>

                {loading ? (
                    <p>Cargando tareas...</p>
                ) : (
                    tasks.length === 0 ? <p>No hay tareas</p> : null
                )}
                {/* Sección de tareas "Por hacer" */}
                <section className="mb-6">
                    <h3 className="text-lg font-semibold mb-2">Por hacer</h3>
                    <div className="bg-white shadow-md rounded p-4">
                        {tasksToDo.map(task => (
                            <TodoItem
                                key={task.id}
                                task={task}
                                updateTaskStatus={updateTaskStatus}
                                deleteTask={deleteTask}
                                startEditingTask={startEditingTask}
                            />
                        ))}
                    </div>
                </section>

                {/* Sección de tareas "En curso" */}
                <section className="mb-6">
                    <h3 className="text-lg font-semibold mb-2">En curso</h3>
                    <div className="bg-white shadow-md rounded p-4">
                        {tasksInProgress.map(task => (
                            <TodoItem
                                key={task.id}
                                task={task}
                                updateTaskStatus={updateTaskStatus}
                                deleteTask={deleteTask}
                                startEditingTask={startEditingTask}
                            />
                        ))}
                    </div>
                </section>

                {/* Sección de tareas "Finalizado" */}
                <section className="mb-6">
                    <h3 className="text-lg font-semibold mb-2">Finalizado</h3>
                    <div className="bg-white shadow-md rounded p-4">
                        {tasksDone.map(task => (
                            <TodoItem
                                key={task.id}
                                task={task}
                                updateTaskStatus={updateTaskStatus}
                                deleteTask={deleteTask}
                                startEditingTask={startEditingTask}
                            />
                        ))}
                    </div>
                </section>
            </main>
        </div>
    );
};

export default Dashboard;
