<template>
    <div class="product-card" v-if="product">
        <h2>{{ product.name }}</h2>
        <p>${{ product.price.toFixed(2) }}</p>
        <button @click="handleAddToCart">Add to Cart</button>
    </div>
</template>

<script lang="ts" setup>
    import { defineProps, defineEmits } from 'vue';
    import IProduct from '@/interfaces/IProduct';

    // Define las propiedades del componente
    const props = defineProps<{
        product: IProduct;
    }>();

    // Define los eventos del componente
    const emit = defineEmits<{
        (event: 'addToCart', productName: string, productPrice: number): void;
    }>();

    // Función que maneja el evento de agregar al carrito
    const handleAddToCart = () => {
        emit('addToCart', props.product.name, props.product.price);
    };
</script>

<style scoped> 
    .product-card {
        background-color: #fff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.3s, box-shadow 0.3s;
    }

    .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .product-card h2 {
        margin: 0 0 0.5rem 0;
        font-size: 1.6rem;
        color: #333;
    }

    .product-card p {
        margin: 0 0 1rem 0;
        font-size: 1.2rem;
        color: #666;
    }

    .product-card button {
        padding: 0.75rem 1.5rem;
        border: none;
        background-color: #4a90e2;
        color: #fff;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s, transform 0.2s;
    }

    .product-card button:hover {
        background-color: #357abd;
        transform: scale(1.05);
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
  