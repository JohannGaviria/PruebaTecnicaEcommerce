import { Ref, ref } from 'vue';
import IProduct from '@/interfaces/IProduct';

class ProductService {
    // Define una referencia para almacenar la lista de productos
    private products: Ref<Array<IProduct>>;

    constructor() {
        this.products = ref<Array<IProduct>>([]);
    }

    // Método para obtener la referencia de productos
    getProducts(): Ref<Array<IProduct>> {
        return this.products;
    }

    // Método asíncrono para obtener todos los productos de la API
    async fetchAll(): Promise<void> {
        try {
            const url = 'http://127.0.0.1:8000/api/products/';
            // Envía una solicitud GET a la API para obtener los productos
            const response = await fetch(url);
    
            // Verifica si la respuesta es exitosa
            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }
    
            // Convierte la respuesta en JSON
            const json = await response.json();
    
            // Verifica si los datos contienen una lista de productos
            if (json.data && Array.isArray(json.data.products)) {
                // Actualiza la referencia de productos con los datos obtenidos
                this.products.value = json.data.products.map((product: any) => ({
                    ...product,
                    price: parseFloat(product.price) // Convierte el precio a un número flotante
                }));
            } else {
                console.error('Invalid data received from API');
            }
        } catch (error) {
            console.error('Error fetching products:', error);
        }
    }
}

export default ProductService;
