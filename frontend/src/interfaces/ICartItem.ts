import IProduct from "./IProduct";

// Interfaz para los itmes del carrito
interface ICartItem {
    product: IProduct;
    quantity: number;
}
export default ICartItem;