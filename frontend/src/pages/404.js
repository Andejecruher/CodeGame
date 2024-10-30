// src/pages/404.js
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

export default function Custom404() {
    const router = useRouter();
    const [countdown, setCountdown] = useState(5);

    useEffect(() => {
        if (countdown === 0) {
            router.push('/');
        }

        const timer = setInterval(() => {
            setCountdown(prevCountdown => prevCountdown - 1);
        }, 1000);

        return () => clearInterval(timer); // Limpiar el temporizador al desmontar
    }, [countdown, router]);

    const handleGoHome = () => {
        router.push('/');
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100 p-6">
            <div className="text-center space-y-6">
                <h1 className="text-8xl font-bold text-blue-600">404</h1>
                <h2 className="text-3xl font-semibold text-gray-800">
                    Oops! Página no encontrada
                </h2>
                <p className="text-gray-600">
                    La página que estás buscando no existe o ha sido movida.
                </p>
                <p className="text-gray-500">
                    Redirigiendo al inicio en <span className="font-bold">{countdown}</span> segundos...
                </p>
                <button
                    onClick={handleGoHome}
                    className="mt-6 px-8 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors duration-200"
                >
                    Regresar al inicio ahora
                </button>
            </div>
        </div>
    );
}
