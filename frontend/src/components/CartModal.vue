<template>
    <transition name="modal-fade">
        <div v-if="isVisible" class="modal-overlay" @click="closeModal">
            <div class="modal-content" @click.stop>
                <button class="close-btn" @click="closeModal">&times;</button>
                <h2>Your Cart</h2>
                <div v-if="!isLoggedIn">
                    <p>Please log in to see your cart.</p>
                </div>
                <div v-else>
                    <div v-if="cartProducts.length === 0">
                        <p>Your cart is empty.</p>
                    </div>
                    <div v-else>
                        <div v-for="item in cartProducts" :key="item.product.id" class="cart-item">
                            <p>
                                {{ item.product.name }} ${{ item.product.price.toFixed(2) }} x {{ item.quantity }} 
                                <span class="remove-icon" @click="removeFromCart(item.product.id)">
                                    <i class="fas fa-trash-alt"></i>
                                </span>
                            </p>
                        </div>
                        <button id="order-button" :disabled="cartProducts.length < 1" @click="placeOrder">Place Order</button>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script lang="ts" setup>
    import { defineProps, defineEmits, onMounted, ref } from 'vue';
    import ProductService from '@/services/ProductService';
    import OrderService from '@/services/OrderService';
    import IProduct from '@/interfaces/IProduct';

    // Define las propiedades del componente
    const props = defineProps<{
        isVisible: boolean;
    }>();

    // Define los eventos del componente
    const emit = defineEmits<{
        (event: 'closeCart'): void;
        (event: 'removeFromCart', index: number): void;
        (event: 'placeOrder'): void;
    }>();

    // Instancia de ProductService y OrderService
    const productService = new ProductService();
    const orderService = new OrderService();

    // Referencias reactivas
    const cartProducts = ref<IProduct[]>(productService.getCartProducts().value);
    const isLoggedIn = ref(false);

    // Función para cerrar el modal
    const closeModal = () => {
        emit('closeCart');
    };

    // Función para eliminar un producto del carrito
    const removeFromCart = (productId: number) => {
        // Filtra el carrito para eliminar el producto con el ID proporcionado
        cartProducts.value = cartProducts.value.filter(item => item.product.id !== productId);

        // Actualiza el localStorage con el carrito modificado
        localStorage.setItem('cart', JSON.stringify(cartProducts.value));

        // Emite el evento para eliminar el producto del carrito
        emit('removeFromCart', productId);
    };

    // Función para realizar un pedido
    const placeOrder = async () => {
        // Verifica que el usuario este auntenticado
        if (!isLoggedIn.value) {
            alert('Please log in to place an order.');
            return;
        }

        try {
            // Prepara los datos del pedido
            const orderData = {
                items: cartProducts.value.map(item => ({
                    product: item.product.id,
                    quantity: item.quantity
                })),
                total: cartProducts.value.reduce((acc, item) => acc + item.product.price * item.quantity, 0).toFixed(2)
            };

            // Realiza el pedido
            await orderService.createOrder(orderData);

            // Limpia el carrito
            cartProducts.value = [];
            localStorage.removeItem('cart');

            // Cierra el modal
            closeModal();
            alert('Order placed successfully!');
        } catch (error) {
            alert('There was an error placing your order. Please try again.');
        }
    };

    // Verifica que el usuario este auntenticado y obtiene los productos del carrito
    onMounted(async () => {
        const token = localStorage.getItem('token');
        if (token) {
            isLoggedIn.value = true;
            await productService.fetchCart();
            cartProducts.value = productService.getCartProducts().value;
        } else {
            isLoggedIn.value = false;
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
