<template>
    <header>
        <h1>Mini Ecommerce</h1>
        <div class="cart-icon" :class="cartIconClass" @click="handleClick">🛒</div>
    </header>
</template>

<script lang="ts" setup>
    import { defineProps, defineEmits, PropType } from 'vue';

    // Define las propiedades del componente
    const props = defineProps<{
        cartIconClass?: { [key: string]: boolean };
    }>();

    // Define los eventos del componente
    const emit = defineEmits<{
        (event: 'openCart'): void;
    }>();

    // Función que maneja el evento 'openCart'
    const handleClick = () => {
        emit('openCart');
    };
</script>


<style scoped>
    .cart-icon {
        cursor: pointer;
        font-size: 1.8rem;
        transition: transform 0.3s;
    }

    .cart-icon.vibrate {
        animation: vibrate 0.3s linear;
    }

    @keyframes vibrate {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-2px); }
        50% { transform: translateX(2px); }
        75% { transform: translateX(-2px); }
    }
</style>
