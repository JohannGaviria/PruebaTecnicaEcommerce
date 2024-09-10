<template>
    <main>
        <div class="product-grid">
            <ProductCard
                v-for="(product, index) in products"
                :key="index"
                :product="product"
                @addToCart="addToCart"
            />
        </div>
    </main>
</template>
    
<script lang="ts" setup>
    import { ref, defineEmits } from 'vue';
    import ProductCard from './ProductCard.vue';

    // Interfaz que define la estructura de un producto
    interface Product {
        name: string;
        price: number;
    }

    // Define los eventos del componente
    const emit = defineEmits<{
        (event: 'addToCart', productName: string, productPrice: number): void;
    }>();

    // Define la lista de productos
    const products = ref<Product[]>([
        { name: 'Product 1', price: 10 },
        { name: 'Product 2', price: 15 },
        { name: 'Product 3', price: 20 },
        { name: 'Product 4', price: 25 },
        { name: 'Product 5', price: 30 }
    ]);

    // Función que maneja el evento 'addToCart'
    const addToCart = (productName: string, productPrice: number) => {
        emit('addToCart', productName, productPrice);
    };

    // Define los componentes utilizados en este componente
    const components = {
        ProductCard
    };
</script>

    
<style scoped>
    .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
    }
</style>    