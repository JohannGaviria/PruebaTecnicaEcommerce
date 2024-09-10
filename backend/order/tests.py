from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse
from products.models import Product
from users.models import User
from cart.models import Cart
from .models import Order, OrderItem


# Tests para la creación de ordenes
class CreateOrderTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create_order')
        self.user = User.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.product = Product.objects.create(name='Test Product', price=100, availability=10)
        self.cart = Cart.objects.create(user=self.user)
        self.cart.items.create(product=self.product, quantity=5)


    # Prueba para crear una orden exitosamente
    def test_create_order_success(self):
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba para crear una orden con el carrito vacio
    def test_create_order_cart_empty(self):
        self.cart.items.all().delete()
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)

    
    # Prueba para crear una orden con disponobilidad insuficiente
    def test_create_order_insufficient_availability(self):
        self.cart.items.create(product=self.product, quantity=15)
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)

    
    # Prueba para crear una orden sin token
    def test_create_order_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# Tests para el detalle de una orden
class OrderDetailTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invalid_url = reverse('order_detail', args=[999])
        self.user = User.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.product = Product.objects.create(name='Test Product', price=100, availability=10)
        self.cart = Cart.objects.create(user=self.user)
        self.cart.items.create(product=self.product, quantity=5)
        self.order = Order.objects.create(user=self.user, total=self.product.price * 5)
        OrderItem.objects.create(order=self.order, product=self.product, quantity=5, price=self.product.price * 5)
        self.url = reverse('order_detail', args=[self.order.id])


    # Prueba para obtener detalles de una orden exitosamente
    def test_order_detail_success(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba para obtener detalles de una orden que no existe
    def test_order_detail_not_found(self):
        response = self.client.get(self.invalid_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)

    
    # Prueba para obtener detalles de una orden sin token
    def test_order_detail_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
