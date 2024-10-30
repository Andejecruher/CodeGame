// src/api/axiosInstance.js
import axios from 'axios';
import Cookies from 'js-cookie'; // Usaremos js-cookie para gestionar las cookies del token
import { useRouter } from 'next/router';

const API_URL = 'http://127.0.0.1:5000';

const axiosInstance = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Interceptor para configurar el token en cada solicitud
axiosInstance.interceptors.request.use(
    (config) => {
        const token = Cookies.get('token_codeGame'); // Obtén el token de la cookie
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

// Interceptor para manejar errores de respuesta
axiosInstance.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response && error.response.status === 401) {
            // Si el token ha caducado, elimina la cookie y redirige al login
            Cookies.remove('token_codeGame');
            if (typeof window !== 'undefined') {
                // Redirige al usuario al login si está en el navegador
                const router = useRouter();
                router.push('/login');
            }
        }
        return Promise.reject(error);
    }
);

export default axiosInstance;
