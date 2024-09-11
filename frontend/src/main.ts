import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import LoginService from '@/services/LoginService';

createApp(App).use(router).mount('#app')

// Verifica si el token ha expirado
if (LoginService.isTokenExpired()) {
    // Elimina el token y los datos del usuario del localStorage
    LoginService.logout();
    
    // Redirige a la página de login
    router.push('/login');
}
