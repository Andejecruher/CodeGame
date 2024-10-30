// Este es un contexto que maneja la autenticación de los usuarios.
// Se encarga de guardar el token y los datos del usuario en las cookies, y de proveer funciones para hacer login y logout.
import { createContext, useContext, useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import Cookies from 'js-cookie';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const router = useRouter();
    const [token, setToken] = useState(null);
    const [user, setUser] = useState(null);

    useEffect(() => {
        const storedToken = Cookies.get('token_codeGame');
        const storedUser = Cookies.get('user_codeGame');
        if (storedToken && storedUser) {
            setToken(storedToken);
            setUser(JSON.parse(storedUser));
        }
    }, [router]);

    const login = (newToken, userData) => {
        Cookies.set('token_codeGame', newToken, { expires: 7 }); // La cookie expira en 7 días
        Cookies.set('user_codeGame', JSON.stringify(userData), { expires: 7 });
        setToken(newToken);
        setUser(userData);
        router.push('/');
    };

    const logout = () => {
        Cookies.remove('token_codeGame');
        Cookies.remove('user_codeGame');
        setToken(null);
        setUser(null);
        router.push('/auth/login');
    };

    return (
        <AuthContext.Provider value={{ token, user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);