<template>
    <div id="app">
        <HeaderComponent
            :cartIconClass="{ 'vibrate': isCartVibrating }"
            @openCart="openCart"
        />
        <MainComponent @addToCart="handleAddToCart" />
        <CartModal
            :isVisible="isCartVisible"
            :cart="cartItems"
            @closeCart="closeCart"
            @removeFromCart="removeFromCart"
            @placeOrder="handlePlaceOrder"
        />
    </div>
</template>

<script lang="ts" setup>
    import { ref, nextTick } from 'vue';
    import HeaderComponent from '@/components/HeaderComponent.vue';
    import MainComponent from '@/components/MainComponent.vue';
    import CartModal from '@/components/CartModal.vue';

    // Estado para controlar la visibilidad del carrito
    const isCartVisible = ref(false);

    // Estado para almacenar los ítems del carrito
    const cartItems = ref<Array<{ id: number; name: string; price: number }>>([]);

    // Estado para manejar la vibración del carrito
    const isCartVibrating = ref(false);

    // Función para abrir el carrito
    const openCart = () => {
        isCartVisible.value = true;
    };

    // Función para cerrar el carrito
    const closeCart = () => {
        isCartVisible.value = false;
    };

    // Función para agregar un producto al carrito
    const handleAddToCart = (productName: string, productPrice: number) => {
        cartItems.value.push({ id: cartItems.value.length + 1, name: productName, price: productPrice });
        triggerCartVibration();
    };

    // Función para activar la vibración del carrito
    const triggerCartVibration = () => {
        isCartVibrating.value = true;
        nextTick(() => {
            setTimeout(() => {
                isCartVibrating.value = false;
            }, 300);
        });
    };

    // Función para eliminar un ítem del carrito
    const removeFromCart = (index: number) => {
        cartItems.value.splice(index, 1);
    };

    // Función para realizar el pedido y vaciar el carrito
    const handlePlaceOrder = () => {
        console.log('Order placed:', cartItems.value);
        cartItems.value = [];
        isCartVisible.value = false;
        alert('Your order has been placed successfully!');
    };

    // Define los componentes utilizados en este componente
    const components = {
        HeaderComponent,
        MainComponent,
        CartModal
    };
</script>


<style scoped>
    .vibrate {
        animation: vibrate 0.3s linear;
    }

    @keyframes vibrate {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-2px); }
        50% { transform: translateX(2px); }
        75% { transform: translateX(-2px); }
    }
</style>
