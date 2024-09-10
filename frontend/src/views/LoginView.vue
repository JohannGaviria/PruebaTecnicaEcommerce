<template>
    <div id="login">
        <h2>Login</h2>
        <AuthForm @submit="handleLogin" />
    </div>
</template>
  
<script lang="ts" setup>
    import AuthForm from '@/components/AuthComponent.vue';

    // Función que maneja el login
    const handleLogin = (formData: { email: string; password: string }) => {
        console.log('Login with:', formData);
    };

    // Define los componentes utilizados en este componente
    const components = {
        AuthForm
    };
</script>

  
<style scoped>
    #login {
        max-width: 400px;
        margin: auto;
    }
</style>
  