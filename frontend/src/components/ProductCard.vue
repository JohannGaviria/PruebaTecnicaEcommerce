<template>
    <div class="product-card" v-if="product">
        <h2>{{ product.name }}</h2>
        <p>${{ product.price.toFixed(2) }}</p>
        {{ product.availability }} /
        <input type="number" v-model="quantity" min="1" max="{{ product.availability }}" />
        <button id="add-cart-btn" :disabled="product.availability < 1" @click="handleAddToCart">Add to Cart</button>
    </div>
</template>

<script lang="ts" setup>
    import { ref, defineProps, defineEmits } from 'vue';
    import IProduct from '@/interfaces/IProduct';
    import ProductService from '@/services/ProductService';

    // Define las propiedades del componente
    const props = defineProps<{
        product: IProduct;
    }>();

    // Define la cantidad del producto a agregar al carrito
    const quantity = ref(1);

    // Obtén una instancia del ProductService
    const productService = new ProductService();

    // Función que maneja el evento de agregar al carrito
    const handleAddToCart = async () => {
        await productService.addToCart(props.product.id, quantity.value);
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

    .product-card input {
        width: 10%;
        margin-bottom: 10px;
    }
    
    .product-card button {
        width: 100%;
        padding: 0.75rem 1.5rem;
        margin-top: 15px;
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

    #add-cart-btn:disabled {
        background-color: #ccc;
        cursor: not-allowed;
        color: #1b1b1b;
    }
</style>
