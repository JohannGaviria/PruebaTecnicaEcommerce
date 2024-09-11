import { Ref, ref } from 'vue';
import IOrder from '@/interfaces/IOrder';

class OrderService {
    // Variable privada para manejar las órdenes
    private orders: Ref<Array<IOrder>>;
    private orderUpdatedCallback: (() => void) | null = null;

    constructor() {
        this.orders = ref<Array<IOrder>>([]);
    }

    // Devuelve las órdenes
    getOrders(): Ref<Array<IOrder>> {
        return this.orders;
    }

    // Establece una función de callback para cuando se actualice una orden
    setOrderUpdatedCallback(callback: () => void) {
        this.orderUpdatedCallback = callback;
    }

    // Notifica que se ha actualizado una orden
    private notifyOrderUpdated() {
        if (this.orderUpdatedCallback) {
            this.orderUpdatedCallback();
        }
    }

    // Crea una nueva orden
    async createOrder(orderData: any): Promise<void> {
        try {
            const token = localStorage.getItem('token');
            if (!token) {
                throw new Error('User not authenticated');
            }

            const url = 'http://127.0.0.1:8000/api/order/';
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`
                },
                body: JSON.stringify(orderData)
            });

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || 'Error creating order');
            }

            if (json.data && json.data.order) {
                this.orders.value.push(json.data.order);
                this.notifyOrderUpdated();
            } else {
                console.error('Invalid data received from API');
            }
        } catch (error) {
            alert(`Error creating order: ${error}`);
        }
    }

    // Recupera una orden por su ID
    async fetchOrderById(orderId: number): Promise<void> {
        try {
            const token = localStorage.getItem('token');
            if (!token) {
                throw new Error('User not authenticated');
            }

            const url = `http://127.0.0.1:8000/api/order/${orderId}`;
            const response = await fetch(url, {
                headers: {
                    'Authorization': `Token ${token}`
                }
            });

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || 'Error getting order');
            }

            if (json.data && json.data.order) {
                const orderIndex = this.orders.value.findIndex(order => order.id === orderId);
                if (orderIndex !== -1) {
                    this.orders.value[orderIndex] = json.data.order;
                } else {
                    this.orders.value.push(json.data.order);
                }
                this.notifyOrderUpdated();
            } else {
                console.error('Invalid data received from API');
            }
        } catch (error) {
            alert(`Error fetching order by ID: ${error}`);
        }
    }
}

export default OrderService;
