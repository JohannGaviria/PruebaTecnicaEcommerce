from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer


# Endpoint para crear un pedido
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request):
    try:
        # Buscar el carrito del usuario
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        # Respuesta erronea del endpoint
        return Response({
            'status': 'error',
            'message': 'cart is empty'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Verificar si el carrito está vacío
    if not cart.items.exists():
        return Response({
            'status': 'error',
            'message': 'cart is empty'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Crea la orden
    order = Order.objects.create(user=request.user, total=0)
    total = 0

    # Itera por cada uno de los productos del carrito
    for item in cart.items.all():
        # Verifica que el producto tenga la disponibilidad correcta
        if item.quantity > item.product.availability:
            return Response({
                'status': 'error',
                'message': f'not enough availability for product {item.product.name}'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Calcula el total de la orden
        price = item.product.price * item.quantity
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=price)
        total += price

        # Descuenta la disponiblidad del producto
        item.product.availability -= item.quantity
        item.product.save()
    
    # Guarda el total de la orden
    order.total = total
    order.save()

    # Limpia el carrito
    cart.items.clear()
    
    # Serializa los datos de la orden
    serializer = OrderSerializer(order)

    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'order created successfully',
        'data': {
            'order': serializer.data
        }
    }, status=status.HTTP_201_CREATED)


# Endpoint para obtener el detalle de un pedido
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_detail(request, order_id):
    try:
        # Obtiene la orden correspodiente al ID
        order = Order.objects.get(id=order_id, user=request.user)
    except Order.DoesNotExist:
        # Respuesta erronea al no encontrar la orden
        return Response({
            'status': 'error',
            'message': 'Order not found'
        }, status=status.HTTP_404_NOT_FOUND)

    # Serializa los datos de la orden
    serializer = OrderSerializer(order)

    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'order successfully obtained',
        'data': {
            'order': serializer.data
        }
    }, status=status.HTTP_200_OK)
