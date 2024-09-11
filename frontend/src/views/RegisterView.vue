<template>
    <div id="register">
        <h2>Register</h2>
            <AuthForm :isRegister="true" @submit="handleRegister" />
        </div>
</template>
  
<script lang="ts" setup>
    import AuthForm from '@/components/AuthComponent.vue';
    import RegisterService from '@/services/RegisterService';
    
    // Función que maneja el registro de usuario
    const handleRegister = async (formData: { username: string; email: string; password: string }) => {
        try {
            await RegisterService.register(formData.username, formData.email, formData.password);
        } catch (error) {
            console.error('Register error:', error);
        }
    };
</script>
  
<style scoped>
    #register {
        max-width: 400px;
        margin: auto;
}
</style>
  