from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from .models import Cart
from .serializers import CartSerializer, CartItemSerializer


# Endpoint para añadir productos al carrito
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_product_cart(request):
    # Obtiene los datos enviados en la solicitud
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')

    try:
        # Obtiene el producto segun el ID que se le pase
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        # Respuesta erronea a no encontrar el producto segun el ID
        return Response({
            'status': 'error',
            'message': 'product not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Verifica que el producto este disponible
    if not product.availability:
        return Response({
            'status': 'error',
            'message': 'Product is not available'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Verifica que la cantidad no supere la disponibilidad
    if int(quantity) > product.availability:
        return Response({
            'status': 'error',
            'message': 'Quantity exceeds available stock'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Obtiene o crea el carrito del usuario
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Obtiene o crea un ítem en el carrito para el producto
    cart_item, created = cart.items.get_or_create(product=product)

    # Verifica que el ítem ya exista en el carrtio
    if not created:
        cart_item.quantity += int(quantity) # Incrementa la cantidad
    else:
        cart_item.quantity = int(quantity) # Establece la cantidad inicial

    # Guardar los cambios en el ítem del carrito
    cart_item.save()

    # Descuenta la cantidad del item a la disponibilidad del producto
    product.availability -= quantity
    # Guarda la nueva disponibilidad
    product.save()

    # Serializa los datos del carrito
    cart_serializer = CartSerializer(cart)

    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'product added to cart successfully',
        'data': {
            'cart': cart_serializer.data
        }
    }, status=status.HTTP_201_CREATED)


# Endpoint para obtener los productos añadidos al carrito
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_cart_list(request):
    try:
        # Obtenemos el carrito del usuario autenticado
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        # Respuesta erronea del endpoint
        return Response({
            'status': 'error',
            'message': 'Cart is empty'
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Serializa los datos del carrito
    serializer = CartSerializer(cart)

    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'products added to cart successfully obtained',
        'data': {
            'cart': serializer.data
        }
    }, status=status.HTTP_200_OK)
