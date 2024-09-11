import { Ref, ref } from 'vue';
import IProduct from '@/interfaces/IProduct';
import ICartItem from '@/interfaces/ICartItem';

class ProductService {
    // Variables privadas para manejar productos y carrito
    private products: Ref<Array<IProduct>>;
    private cartProducts: Ref<Array<ICartItem>>;
    private cartUpdatedCallback: (() => void) | null = null;

    constructor() {
        this.products = ref<Array<IProduct>>([]);
        this.cartProducts = ref<Array<ICartItem>>([]);
        this.loadCartFromLocalStorage();
    }

    // Devuelve los productos
    getProducts(): Ref<Array<IProduct>> {
        return this.products;
    }

    // Devuelve los productos en el carrito
    getCartProducts(): Ref<Array<ICartItem>> {
        return this.cartProducts;
    }

    // Establece una función de callback para cuando se actualice el carrito
    setCartUpdatedCallback(callback: () => void) {
        this.cartUpdatedCallback = callback;
    }

    // Notifica que el carrito ha sido actualizado
    private notifyCartUpdated() {
        if (this.cartUpdatedCallback) {
            this.cartUpdatedCallback();
        }
    }

    // Recupera todos los productos de la API
    async fetchAll(): Promise<void> {
        try {
            const url = 'http://127.0.0.1:8000/api/products/';
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const json = await response.json();

            if (json.data && Array.isArray(json.data.products)) {
                this.products.value = json.data.products.map((product: any) => ({
                    ...product,
                    price: parseFloat(product.price)
                }));
            } else {
                console.error('Invalid data received from API');
            }
        } catch (error) {
            console.error('Error fetching products:', error);
        }
    }

    // Recupera los productos del carrito desde la API
    async fetchCart(): Promise<void> {
        try {
            const token = localStorage.getItem('token');
            if (!token) {
                throw new Error('User not authenticated');
            }

            const url = 'http://127.0.0.1:8000/api/cart/';
            const response = await fetch(url, {
                headers: {
                    'Authorization': `Token ${token}`
                }
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const json = await response.json();

            if (json.data && json.data.cart && Array.isArray(json.data.cart.items)) {
                this.cartProducts.value = json.data.cart.items.map((item: any) => ({
                    product: {
                        ...item.product,
                        price: parseFloat(item.product.price)
                    },
                    quantity: item.quantity
                }));
                this.saveCartToLocalStorage();
            } else {
                console.error('Invalid data received from API');
            }
        } catch (error) {
            console.error('Error fetching cart products:', error);
            this.cartProducts.value = this.loadCartFromLocalStorage();
        }
    }

    // Añade un producto al carrito
    async addToCart(productId: number, quantity: number): Promise<void> {
        try {
            const token = localStorage.getItem('token');
            if (!token) {
                throw new Error('User not authenticated');
            }

            const url = `http://127.0.0.1:8000/api/cart/add`;
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`
                },
                body: JSON.stringify({ product_id: productId, quantity: quantity })
            });

            const json = await response.json();

            if (!response.ok) {
                if (json.status === 'error' && 
                    (json.message === 'Total quantity in cart exceeds available stock' || 
                     json.message === 'Quantity exceeds available stock')) {
                    alert('The total quantity in the cart exceeds the available stock. Please adjust the quantity.');                
                } else {
                    throw new Error(`Error: ${response.statusText}`);
                }
                return;
            }

            if (json.data && json.data.cart && Array.isArray(json.data.cart.items)) {
                this.cartProducts.value = json.data.cart.items.map((item: any) => ({
                    product: {
                        ...item.product,
                        price: parseFloat(item.product.price)
                    },
                    quantity: item.quantity
                }));
                this.saveCartToLocalStorage();
                this.notifyCartUpdated();
                alert('Item added to cart successfully.')
            } else {
                console.error('Invalid data received from API');
            }
        } catch (error) {
            console.error('Error adding product to cart:', error);
        }
    }

    // Guarda el carrito en el almacenamiento local
    private saveCartToLocalStorage() {
        const cartItems = this.cartProducts.value.map(item => ({
            product: item.product,
            quantity: item.quantity
        }));
        localStorage.setItem('cart', JSON.stringify(cartItems));
    }

    // Carga el carrito desde el almacenamiento local
    private loadCartFromLocalStorage(): Array<ICartItem> {
        const cartItems = localStorage.getItem('cart');
        if (cartItems) {
            return JSON.parse(cartItems).map((item: any) => ({
                product: {
                    ...item.product,
                    price: parseFloat(item.product.price)
                },
                quantity: item.quantity
            }));
        }
        return [];
    }
}

export default ProductService;
