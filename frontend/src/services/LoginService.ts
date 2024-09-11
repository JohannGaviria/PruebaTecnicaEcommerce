class LoginService {
    // Función para realizar el login
    async login(email: string, password: string): Promise<void> {
        try {
            // Envía una solicitud POST al endpoint de login
            const response = await fetch('http://127.0.0.1:8000/api/users/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });

            // Convierte la respuesta en JSON
            const data = await response.json();

            // Verifica si el login fue exitoso
            if (data.status === 'success') {
                const { token, user } = data.data;

                // Guarda el token y los datos del usuario en localStorage
                localStorage.setItem('token', token.token_key);
                localStorage.setItem('user', JSON.stringify(user));

                // Calcula la expiración del token y guarda en localStorage
                const expirationDate = new Date(token.token_expiration);
                localStorage.setItem('token_expiration', expirationDate.toISOString());

                // Redirige a la ruta raíz
                window.location.href = '/';
            } else {
                console.error('Login failed:', data.message);
            }
        } catch (error) {
            console.error('An error occurred:', error);
        }
    }

    // Función para verificar si el token ha expirado
    isTokenExpired(): boolean {
        const expiration = localStorage.getItem('token_expiration');
        if (expiration) {
            const expirationDate = new Date(expiration);
            // Compara la fecha actual con la fecha de expiración
            return new Date() > expirationDate;
        }
        return true;
    }

    
    // Función para eliminar el token y los datos del usuario
    logout(): void {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        localStorage.removeItem('token_expiration');
    }
}

export default new LoginService();
