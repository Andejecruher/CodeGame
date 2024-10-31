// src/pages/index.js
import { useAuth } from '../context/AuthContext';
import TaskForm from '../components/TaskForm';
import TodoItem from '../components/TodoItem';
import { useEffect, useState } from 'react';
import { getTasks, addTask as addTaskApi, updateTask as updateTaskApi, deleteTask as deleteTaskApi } from '../utils/api';

const Dashboard = () => {
    const { user, logout } = useAuth();
    const [tasks, setTasks] = useState([]);
    const [editingTask, setEditingTask] = useState(null);
    const [loading, setLoading] = useState(true);

    const fetchTasks = async () => {
        try {
            const fetchedTasks = await getTasks();
            setTasks(fetchedTasks);
        } catch (error) {
            setError('Failed to fetch tasks');
        } finally {
            setLoading(false);
        }
    };

    const addTask = async (newTask) => {
        try {
            const addedTask = await addTaskApi(newTask.title, newTask.description, newTask.date);
            setTasks([...tasks, addedTask]);
            fetchTasks();
        } catch (error) {
            setError('Failed to add task');
        }
    };

    const updateTask = async (id, updatedTask) => {
        try {
            const updatedTaskData = await updateTaskApi(id, updatedTask.title, updatedTask.description);
            setTasks(tasks.map(task => task.id === id ? updatedTaskData : task));
            fetchTasks();
        } catch (error) {
            setError('Failed to update task');
        }
    };

    const updateTaskStatus = async (id, newStatus) => {
        try {
            const taskToUpdate = tasks.find(task => task.id === id);
            const updatedTask = await updateTaskApi(id, taskToUpdate.title, taskToUpdate.description, newStatus);
            setTasks(tasks.map(task => task.id === id ? updatedTask : task));
            fetchTasks();
        } catch (error) {
            setError('Failed to update task');
        }
    };

    const deleteTask = async (id) => {
        try {
            await deleteTaskApi(id);
            setTasks(tasks.filter(task => task.id !== id));
            fetchTasks();
        } catch (error) {
            setError('Failed to delete task');
        }
    };

    const startEditingTask = (task) => {
        setEditingTask(task);
    };

    const tasksToDo = tasks ? tasks.filter(task => task.status === "Por hacer") : [];
    const tasksInProgress = tasks ? tasks.filter(task => task.status === "En curso") : [];
    const tasksDone = tasks ? tasks.filter(task => task.status === "Finalizado") : [];

    useEffect(() => {
        if(user){
            fetchTasks();
        }
    }, [user]);

    return (
        <div className="min-h-screen bg-gray-100 flex flex-col items-center">
            <header className="bg-blue-600 w-full py-2 sm:py-4 flex justify-between items-center px-2 sm:px-6 text-white">
                <div>
                    <h1 className="text-xl sm:text-2xl font-bold">Bienvenido !</h1>
                    <p>{user?.email}</p>
                </div>
                <button onClick={logout} className="bg-red-500 px-1 py-1 sm:px-4 sm:py-2 rounded">Logout</button>
            </header>

            <main className="w-full max-w-xl lg:max-w-6xl p-4 mt-6">

                <div className="text-center mb-6">
                    <h1 className="text-4xl font-bold text-blue-600">CodeGame Task</h1>
                </div>

                <TaskForm addTask={addTask} updateTask={updateTask} editingTask={editingTask} setEditingTask={setEditingTask} />

                <h2 className="text-2xl font-semibold mb-4">Lista de Tareas</h2>

                {loading ? (
                    <p>Cargando tareas...</p>
                ) : (
                    tasks.length === 0 ? <p>No hay tareas</p> : null
                )}

                {/* Contenedor de las columnas de tareas */}
                <div className="grid gap-6 grid-cols-1 lg:grid-cols-3">
                    {/* Sección de tareas "Por hacer" */}
                    <section className="bg-white shadow-md rounded p-4">
                        <h3 className="text-lg font-semibold mb-4 text-yellow-600">Por hacer</h3>
                        {tasksToDo.map(task => (
                            <TodoItem
                                key={task.id}
                                task={task}
                                updateTaskStatus={updateTaskStatus}
                                deleteTask={deleteTask}
                                startEditingTask={startEditingTask}
                            />
                        ))}
                    </section>

                    {/* Sección de tareas "En curso" */}
                    <section className="bg-white shadow-md rounded p-4">
                        <h3 className="text-lg font-semibold mb-4 text-blue-600">En curso</h3>
                        {tasksInProgress.map(task => (
                            <TodoItem
                                key={task.id}
                                task={task}
                                updateTaskStatus={updateTaskStatus}
                                deleteTask={deleteTask}
                                startEditingTask={startEditingTask}
                            />
                        ))}
                    </section>

                    {/* Sección de tareas "Finalizado" */}
                    <section className="bg-white shadow-md rounded p-4">
                        <h3 className="text-lg font-semibold mb-4 text-green-600">Finalizado</h3>
                        {tasksDone.map(task => (
                            <TodoItem
                                key={task.id}
                                task={task}
                                updateTaskStatus={updateTaskStatus}
                                deleteTask={deleteTask}
                                startEditingTask={startEditingTask}
                            />
                        ))}
                    </section>
                </div>
            </main>
        </div>
    );
};

export default Dashboard;
