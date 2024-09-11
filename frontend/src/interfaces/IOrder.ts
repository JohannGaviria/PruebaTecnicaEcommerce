import IOrderItem from "./IOrderItem";

// Interfaz para la orden
interface IOrder {
    id: number;
    user: number;
    created_at: string;
    total: string;
    items: Array<IOrderItem>;
}
export default IOrder;