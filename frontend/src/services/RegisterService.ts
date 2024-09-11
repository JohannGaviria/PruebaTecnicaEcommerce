class RegisterService {
    // Función para realizar el registro
    async register(username: string, email:string, password: string): Promise<void> {
        try {
            // Envía una solicitud POST al endpoint de register
            const response = await fetch('http://127.0.0.1:8000/api/users/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, email, password }),
            });

            // Convierte la respuesta en JSON
            const data = await response.json();

            // Verifica si el registro fue exitoso
            if (data.status === 'success') {
                // Redirige al login
                window.location.href = '/login'
            }
        } catch (error) {
            console.error('An Error occurred:', error);
        }
    }
}
export default new RegisterService();