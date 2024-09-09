from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import timedelta
from .models import User
from .serializers import UserValidationSerializer, UserSerializer


# Endpoint para el registro de usuarios
@api_view(['POST'])
def register(request):
    # Serializa los datos enviados en la solicitud
    serializer = UserValidationSerializer(data=request.data)

    # Verifica que los datos sean válidos
    if serializer.is_valid():
        # Guarda al usuario
        user = serializer.save()
        
        # Crea un token de autenticación para el usuario
        token = Token.objects.create(user=user)

        # Serializa los datos del usuario
        user_serializer = UserSerializer(user)

        # Respuesta exitosa del endpoint
        return Response({
            'status': 'success',
            'message': 'successful registration',
            'data': {
                'token': {
                    'token_key': token.key
                },
                'user': user_serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Respuesta erronea del endpoint
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Endpoint para el inicio de sesión de usuarios
@api_view(['POST'])
def login(request):
    # Obtiene los datos enviados en la solicitud
    email = request.data.get('email')
    password = request.data.get('password')

    # Autentica al usuario
    user = authenticate(request, username=email, password=password)

    # Verifica la autenticación del usuario
    if user is None:
        # Respuesta de error si la autenticación falla
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'non_field_errors': ['Invalid email or password']
            }
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Crea o actualiza el token del usuario
    token, created = Token.objects.get_or_create(user=user)
    
    # Serializa los datos del usuario
    serializer = UserSerializer(user)

    # Configuración del tiempo de expiración del token
    expiration = timezone.now() + timedelta(days=3)

    # Respuesta exitosa del endpoint
    return Response({
        'status': 'success',
        'message': 'successful login',
        'data': {
            'token': {
                'token_key': token.key,
                'token_expiration': expiration.isoformat()
            },
            'user': serializer.data
        }
    }, status=status.HTTP_200_OK)
