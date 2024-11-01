import { useState } from 'react';
import { useRouter } from 'next/router';
import { register as registerApi } from '../../utils/api';
import Alert from '../../components/Alert';
import { useAuth } from '../../context/AuthContext';

export default function Register() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [alert, setAlert] = useState(null);
    const [loading, setLoading] = useState(false);
    const { login } = useAuth();
    const router = useRouter();

    // Función para validar un correo electrónico
    const validateEmail = (email) => {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    };

    // Función para manejar el envío del formulario
    const handleSubmit = async (e) => {
        e.preventDefault();

        // Validar que se ingresen correo y contraseña
        if (!email || !password) {
            setAlert({ message: 'Correo y contraseña requeridos', type: 'error' });
            return;
        }

        // Validar que el correo sea válido
        if (!validateEmail(email)) {
            setAlert({ message: 'Correo no valido', type: 'error' });
            return;
        }

        setLoading(true);

        try {
            // Llamar a la API para registrar un usuario
            const response = await registerApi(email, password);
            if (response.access_token) {
                // Guardar token y datos del usuario en el contexto
                login(response.access_token, response.user);
                // Mostrar mensaje de éxito y redirigir al dashboard
                setAlert({ message: 'Registro exitoso!', type: 'success' });
                setTimeout(() => {
                    router.push('/');
                }, 2000);
            } else {
                setAlert({ message: 'Error en el registro', type: 'error' });
            }
        } catch (error) {
            setAlert({ message: 'Error en el registro', type: 'error' });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
            <div className="relative py-3 sm:max-w-xl sm:mx-auto">
                <div className="absolute inset-0 bg-gradient-to-r from-blue-300 to-blue-600 shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl"></div>
                <div className="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
                    <div className="max-w-md mx-auto">
                        <div className="text-center mb-6">
                            <h1 className="text-4xl font-bold text-blue-600">CodeGame Task</h1>
                        </div>
                        <div>
                            <h1 className="text-2xl font-semibold">Registro</h1>
                        </div>
                        {alert && <Alert message={alert.message} type={alert.type} />}
                        <div className="divide-y divide-gray-200">
                            <form onSubmit={handleSubmit} className="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                                <div className="relative">
                                    <input
                                        autoComplete="off"
                                        id="email"
                                        name="email"
                                        type="text"
                                        className="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:border-rose-600"
                                        placeholder="Correo electrónico"
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                    />
                                    <label
                                        htmlFor="email"
                                        className="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
                                    >
                                        Correo electrónico
                                    </label>
                                </div>
                                <div className="relative">
                                    <input
                                        autoComplete="off"
                                        id="password"
                                        name="password"
                                        type="password"
                                        className="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:border-rose-600"
                                        placeholder="Contraseña"
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                    />
                                    <label
                                        htmlFor="password"
                                        className="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
                                    >
                                        Contraseña
                                    </label>
                                </div>
                                <div className="relative">
                                    <button type="submit" className="bg-blue-500 text-white rounded-md px-2 py-1 float-right" disabled={loading}>
                                        {loading ? 'Cargando...' : 'Registrarse'}
                                    </button>
                                </div>
                            </form>
                            <div className="mt-4 text-center">
                                <a href="/auth/login" className="text-blue-500 hover:underline">¿Ya tienes una cuenta? Inicia sesión</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}