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
    
<script lang="ts">
    import { defineComponent, ref } from 'vue';
    import ProductCard from './ProductCard.vue';
    
    interface Product {
        name: string;
        price: number;
    }
    
    export default defineComponent({
        components: {
            ProductCard
        },
        setup(_, { emit }) {
            const products = ref<Product[]>([
            { name: 'Product 1', price: 10 },
            { name: 'Product 2', price: 15 },
            { name: 'Product 2', price: 15 },
            { name: 'Product 2', price: 15 },
            { name: 'Product 2', price: 15 }
            ]);
        
            const addToCart = (productName: string, productPrice: number) => {
                emit('addToCart', productName, productPrice);
            };
        
            return {
                products,
                addToCart
            };
        }
    });
</script>
    
<style scoped>
    .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
    }
</style>    