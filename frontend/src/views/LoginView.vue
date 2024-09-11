<template>
    <div id="login">
        <h2>Login</h2>
        <AuthForm @submit="handleLogin" />
    </div>
</template>

<script lang="ts" setup>
    import AuthForm from '@/components/AuthComponent.vue';
    import LoginService from '@/services/LoginService';

    // Función que maneja el login
    const handleLogin = async (formData: { email: string; password: string }) => {
        try {
            await LoginService.login(formData.email, formData.password);
        } catch (error) {
            console.error('Login error:', error);
        }
    };
</script>

<style scoped>
    #login {
        max-width: 400px;
        margin: auto;
    }
</style>
