import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const API_URL = 'http://127.0.0.1:5000'; // Cambia a tu URL de la API

const logout = () => {
    localStorage.removeItem('token_codeGame');
    localStorage.removeItem('user_codeGame');
    router.push('/auth/login');
}

export const login = async (email, password) => {
    const response = await axios.post(`${API_URL}/login`, {
        email,
        password
    }, {
        headers: {
            'Content-Type': 'application/json',
        }
    }).then((res) => {
        return res.data;
    }).catch((error) => {
        return error;
    });


    return response;
};

export const register = async (email, password) => {
    const response = await axios.post(`${API_URL}/register`, {
        email,
        password
    }, {
        headers: {
            'Content-Type': 'application/json',
        }
    }).then((res) => {
        return res.data;
    }).catch((error) => {
        return error;
    });

    return response;
};

export const getTasks = async (token) => {
    const response = await axios.get(`${API_URL}/tasks`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    }).then((res) => {
        return res.data;
    }
    ).catch((error) => {
        if (error.response.status === 401) {
            logout();
        }
        return error;
    });
    return response;
};

export const addTask = async (token, title, description, date) => {
    const response = await axios.post(`${API_URL}/tasks`, {
        title,
        description,
        date
    }, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    }).then((res) => {
        return res.data;
    }
    ).catch((error) => {
        return error;
    });
    return response;
};

export const updateTask = async (token, taskId, title, description, status) => {
    const response = await axios.put(`${API_URL}/tasks/${taskId}`, {
        title,
        description,
        status
    }, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    }).then((res) => {
        return res.data;
    }).catch((error) => {
        return error;
    });
    return response;
};

export const deleteTask = async (token, taskId) => {
    const response = await axios.delete(`${API_URL}/tasks/${taskId}`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    }).then((res) => {
        return res.data;
    }).catch((error) => {
        return error;
    });
    return response;
};