import { createContext, useContext, useEffect, useState } from 'react';
import { useRouter } from 'next/router';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const router = useRouter();
    const [token, setToken] = useState(null);
    const [user, setUser] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem('token_codeGame');
        const user = localStorage.getItem('user_codeGame');
        if (token && user) {
            setToken(token);
            setUser(JSON.parse(user));
        }
    }
    , [router]);

    const login = (newToken, userData) => {
        localStorage.setItem('token_codeGame', newToken);
        localStorage.setItem('user_codeGame', JSON.stringify(userData));
        setToken(newToken);
        setUser(userData);
        router.push('/dashboard');
    };

    const logout = () => {
        router.push('/auth/login');
        setTimeout(() => {
            localStorage.removeItem('token_codeGame');
            localStorage.removeItem('user_codeGame');
            setToken(null);
            setUser(null);
        });
        
    };

    return (
        <AuthContext.Provider value={{ token, user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);