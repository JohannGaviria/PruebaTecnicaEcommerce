// Interfaz para los items de la orden
interface IOrderItem {
    product: {
        id: number;
        name: string;
        price: number;
        availability: number;
    };
    quantity: number;
    price: number;
}
export default IOrderItem;