<template>
    <transition
        name="modal-fade"
    >
        <div v-if="isVisible" class="modal-overlay" @click="closeModal">
            <div class="modal-content" @click.stop>
                <button class="close-btn" @click="closeModal">&times;</button>
                <h2>Your Cart</h2>
                <ul>
                    <li v-for="(item, index) in cart" :key="index">
                        {{ item.name }} - ${{ item.price.toFixed(2) }}
                        <span class="remove-icon" @click="removeFromCart(index)">
                            <i class="fas fa-trash-alt"></i>
                        </span>
                    </li>
                </ul>
                <button id="order-button" :disabled="cart.length < 1" @click="placeOrder">Place Order</button>
            </div>
        </div>
    </transition>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';

export default defineComponent({
    props: {
        isVisible: {
            type: Boolean,
            required: true
        },
        cart: {
            type: Array as PropType<Array<{ id: number, name: string, price: number }>>,
            required: true
        }
    },
    emits: ['closeCart', 'removeFromCart', 'placeOrder'],
    setup(props, { emit }) {
        const closeModal = () => {
            emit('closeCart');
        };

        const removeFromCart = (index: number) => {
            emit('removeFromCart', index);
        };

        const placeOrder = () => {
            emit('placeOrder');
        };

        return {
            closeModal,
            removeFromCart,
            placeOrder
        };
    }
});
</script>

<style scoped>
    .modal-overlay {
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal-content {
        background-color: #fff;
        padding: 2rem;
        border-radius: 12px;
        width: 90%;
        max-width: 600px;
        text-align: center;
        position: relative;
        animation: slide-in 0.3s ease-out;
    }

    .close-btn {
        position: absolute;
        top: 10px;
        right: 10px;
        background: #e74c3c;
        color: #fff;
        border: none;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }

    .close-btn:hover {
        background: #c0392b;
    }

    #order-button {
        border: none;
        background-color: #4a90e2;
        color: #fff;
        cursor: pointer;
        font-size: 1rem;
        display: inline-block;
        margin-top: 1.5rem;
        transition: background-color 0.3s, transform 0.2s;
        padding: 0.5rem 1rem;
        border-radius: 4px;
    }

    #order-button:hover {
        background-color: #357abd;
    }

    .remove-icon {
        cursor: pointer;
        color: #4a90e2;
        transition: color 0.3s;
    }

    .remove-icon:hover {
        color: #357abd;
    }

    .modal-fade-enter-active, .modal-fade-leave-active {
        transition: opacity 0.5s;
    }

    .modal-fade-enter, .modal-fade-leave-to {
        opacity: 0;
    }

    #order-button:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        color: #1b1b1b;
    }
</style>
