<template>
    <div id="register">
        <h2>Register</h2>
            <AuthForm :isRegister="true" @submit="handleRegister" />
        </div>
</template>
  
<script lang="ts" setup>
    import AuthForm from '@/components/AuthComponent.vue';

    // Función que maneja el registro de usuario
    const handleRegister = (formData: { username: string; email: string; password: string }) => {
        console.log('Register with:', formData);
    };

    // Define los componentes utilizados en este componente
    const components = {
        AuthForm
    };
</script>

  
<style scoped>
    #register {
        max-width: 400px;
        margin: auto;
}
</style>
  