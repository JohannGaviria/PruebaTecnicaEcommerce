<template>
    <div id="register">
        <h2>Register</h2>
            <AuthForm :isRegister="true" @submit="handleRegister" />
        </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';
    import AuthForm from '@/components/AuthComponent.vue';
  
    export default defineComponent({
        name: 'RegisterView',
        components: {
            AuthForm
        },
        setup() {
            const handleRegister = (formData: { username: string, email: string, password: string }) => {
                console.log('Register with:', formData);
            };
    
            return {
                handleRegister
            };
        }
    });
</script>
  
<style scoped>
    #register {
        max-width: 400px;
        margin: auto;
}
</style>
  