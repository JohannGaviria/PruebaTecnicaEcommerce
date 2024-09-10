from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from .models import Cart
from django.db import models
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
        # Obtiene el producto según el ID que se le pase
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        # Respuesta de error si no se encuentra el producto
        return Response({
            'status': 'error',
            'message': 'Product not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Verifica que el producto esté disponible
    if not product.availability:
        return Response({
            'status': 'error',
            'message': 'Product is not available'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Convierte la cantidad a entero
    quantity = int(quantity)

    # Verifica que la cantidad no supere la disponibilidad
    if quantity > product.availability:
        return Response({
            'status': 'error',
            'message': 'Quantity exceeds available stock'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Obtiene o crea el carrito del usuario
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Obtiene el ítem del carrito para el producto
    cart_item, created = cart.items.get_or_create(product=product)

    # Verifica la cantidad total en el carrito
    total_quantity = cart.items.filter(product=product).aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0
    if total_quantity + quantity > product.availability:
        return Response({
            'status': 'error',
            'message': 'Total quantity in cart exceeds available stock'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Verifica que el ítem ya exista en el carrito
    if not created:
        cart_item.quantity += quantity  # Incrementa la cantidad
    else:
        cart_item.quantity = quantity  # Establece la cantidad inicial

    # Guarda los cambios en el ítem del carrito
    cart_item.save()

    # Serializa los datos del carrito
    cart_serializer = CartSerializer(cart)

    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'Product added to cart successfully',
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
