from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.utils import get_paginated
from .models import Product
from .serializers import ProductSerializer


# Endpoint para obtener lista de productos
@api_view(['GET'])
def product_list(request):
    # Obtiene todos los productos
    products = Product.objects.all().order_by('id')
    
    # Obtiene la página solicitada a la paginación
    # page = get_paginated(request, products, 10) # Muestra 10 productos por página

    # Serializa los datos de los productos
    serializer = ProductSerializer(products, many=True) # Cambiar products por page para urtilizar la paginacion
    
    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'successfully obtained product list',
        'data': {
            'products': serializer.data
        }
    }, status=status.HTTP_200_OK)
