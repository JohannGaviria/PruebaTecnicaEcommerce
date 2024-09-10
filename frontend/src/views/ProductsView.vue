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

<script lang="ts">
    import { defineComponent, ref, nextTick } from 'vue';
    import MainComponent from '@/components/MainComponent.vue';
    import CartModal from '@/components/CartModal.vue';
    import HeaderComponent from '@/components/HeaderComponent.vue';

    export default defineComponent({
        components: {
            HeaderComponent,
            MainComponent,
            CartModal
        },
        setup() {
            const isCartVisible = ref(false);
            const cartItems = ref<Array<{ id: number, name: string, price: number }>>([]);
            const isCartVibrating = ref(false);

            const openCart = () => {
                isCartVisible.value = true;
            };

            const closeCart = () => {
                isCartVisible.value = false;
            };

            const handleAddToCart = (productName: string, productPrice: number) => {
                cartItems.value.push({ id: cartItems.value.length + 1, name: productName, price: productPrice });
                triggerCartVibration();
            };

            const triggerCartVibration = () => {
                isCartVibrating.value = true;
                nextTick(() => {
                    setTimeout(() => {
                        isCartVibrating.value = false;
                    }, 300);
                });
            };

            const removeFromCart = (index: number) => {
                cartItems.value.splice(index, 1);
            };

            const handlePlaceOrder = () => {
                console.log('Order placed:', cartItems.value);
                cartItems.value = [];
                isCartVisible.value = false;
                alert('Your order has been placed successfully!');
            };

            return {
                isCartVisible,
                cartItems,
                isCartVibrating,
                openCart,
                closeCart,
                handleAddToCart,
                removeFromCart,
                handlePlaceOrder
            };
        }
    });
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
