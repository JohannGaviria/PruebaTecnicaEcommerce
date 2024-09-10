<template>
    <form @submit.prevent="handleSubmit" class="form">

        <div v-if="isRegister" class="form-group">
            <input type="text" id="username" class="form-input" placeholder=" " v-model="formData.username" required />
            <label for="username" class="form-label">Username:</label>
            <i class="fas fa-user-circle input-icon"></i>
        </div>

        <div class="form-group">
            <input type="email" id="email" class="form-input" placeholder=" " v-model="formData.email" required>
            <label for="email" class="form-label">Email:</label>
            <i class="fas fa-message input-icon"></i>
        </div>

        <div class="form-group">
            <input type="password" id="password" class="form-input" placeholder=" " v-model="formData.password" required>
            <label for="password" class="form-label">Password:</label>
            <i class="fas fa-lock input-icon"></i>
        </div>
        <button type="submit" class="btn-send">{{ isRegister ? 'Register' : 'Login' }}</button>
    </form>
</template>
  
<script lang="ts">
    import { defineComponent, ref } from 'vue';
  
    export default defineComponent({
        name: 'AuthForm',
        props: {
            isRegister: {
                type: Boolean,
                default: false
            }
        },
        setup(props, { emit }) {
            const formData = ref({
                username: '',
                email: '',
                password: ''
            });

            const handleSubmit = () => {
                emit('submit', formData.value);
            };

            return {
                formData,
                handleSubmit
            };
        }
    });
</script>
  
<style scoped>
    .form {
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #4180c7;
        box-shadow: 0px 0px 10px rgba(219, 219, 219, 0.1);
        width: 400px;
    }

    .form-group {
        position: relative;
        margin-top: 30px;
        width: 95%;
    }

    .form-input {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #4180c7;
        font-size: 16px;
    }

    .form-label {
        position: absolute;
        top: 50%;
        left: 10px;
        transform: translateY(-50%);
        transition: all 0.3s ease;
        pointer-events: none;
        color: #4a90e2;
    }

    .form-input:focus+.form-label,
    .form-input:not(:placeholder-shown)+.form-label {
        top: -15px;
        left: 0px;
        font-size: 16px;
        padding: 0 5px;
        color: #4180c7;
    }

    .input-icon {
        position: absolute;
        top: 50%;
        right: 10px;
        transform: translateY(-50%);
        cursor: pointer;
        color: #4a90e2;
    }

    .btn-send {
        margin-top: 30px;
        width: 100%;
        padding: 10px;
        background-color: #4a90e2;
        border: none;
        border-radius: 5px;
        color: #fff;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .btn-send:hover {
        background-color: #4180c7;
    }
</style>
