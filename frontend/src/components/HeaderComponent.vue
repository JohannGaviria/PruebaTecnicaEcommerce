<template>
    <header>
        <h1>Mini Ecommerce</h1>
        <div class="cart-icon" :class="cartIconClass" @click="handleClick">🛒</div>
    </header>
</template>

<script lang="ts">
    import { defineComponent, PropType } from 'vue';

    export default defineComponent({
        props: {
            cartIconClass: {
                type: Object as PropType<{ [key: string]: boolean }>,
                required: false
            }
        },
        emits: ['openCart'],
        setup(_, { emit }) {
            const handleClick = () => {
                emit('openCart');
            };

            return {
                handleClick
            };
        }
    });
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
