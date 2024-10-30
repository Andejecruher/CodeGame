// Este archivo es el punto de entrada de la aplicación y se utiliza para envolver todos los componentes de la aplicación con el contexto de autenticación.
// La función AuthProvider se encarga de proveer el contexto de autenticación a todos los componentes de la aplicación.
import { AuthProvider } from '../context/AuthContext';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
    return (
        // Envolver la aplicación con el contexto de autenticación
        <AuthProvider>
            <Component {...pageProps} />
        </AuthProvider>
    );
}

export default MyApp;
