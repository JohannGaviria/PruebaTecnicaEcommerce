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
    import { ref, defineEmits, onMounted } from 'vue';
    import ProductCard from './ProductCard.vue';
    import IProduct from '@/interfaces/IProduct';
    import ProductService from '@/services/ProductService';

    // Define los eventos del componente
    const emit = defineEmits<{
        (event: 'addToCart', productName: string, productPrice: number): void;
    }>();

    const productService = new ProductService();
    const products = ref<IProduct[]>([]);

    // Obtiene los productos desde el sevidor
    onMounted(async () => {
        await productService.fetchAll();
        products.value = productService.getProducts().value;
    });

    // Función que maneja el evento 'addToCart'
    const addToCart = (productName: string, productPrice: number) => {
        emit('addToCart', productName, productPrice);
    };
</script>

    
<style scoped>
    .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
    }
</style>    
