<template>
    <div id="login">
        <h2>Login</h2>
        <AuthForm @submit="handleLogin" />
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';
    import AuthForm from '@/components/AuthComponent.vue';
    
    export default defineComponent({
        name: 'LoginView',
        components: {
            AuthForm
        },
        setup() {
            const handleLogin = (formData: { email: string, password: string }) => {
            console.log('Login with:', formData);
        };
    
        return {
            handleLogin
        };
        }
    });
</script>
  
<style scoped>
    #login {
        max-width: 400px;
        margin: auto;
    }
</style>
  