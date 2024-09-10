from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse
from products.models import Product
from users.models import User
from .models import Cart


# Tests para agregar productos al carrito
class AddProductCartTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('add_product_cart')
        self.user = User.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.product = Product.objects.create(name='Test Product', price=100, availability=10)
        self.data = {
            'product_id': self.product.id,
            'quantity': 5
        }


    # Prueba de agregar producto al carrito exitosamente
    def test_add_product_cart_success(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de agregar producto al carrito no encontrado
    def test_add_product_cart_product_not_found(self):
        self.data['product_id'] = 9999
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de agregar producto al carrito no disponible
    def test_add_product_cart_product_not_available(self):
        self.product.availability = 0
        self.product.save()
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de agregar producto al carrito excede el stock
    def test_add_product_cart_quantity_exceeds_stock(self):
        self.data['quantity'] = 15
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba agregar producto al carrito incrementa la cantidad
    def test_add_product_cart_increment_quantity(self):
        self.client.post(self.url, self.data, format='json')
        self.data['quantity'] = 3
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.first().quantity, 8)
    

    # Prueba de agregar producto al carrito sin token
    def test_add_product_cart_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# Tests para la lista de productos en el carrito
class ProductCartListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('product_cart_list')
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


    # Prueba de productos en el carrito exitosa
    def test_product_cart_list_success(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de productos en el carrito vacia
    def test_product_cart_list_empty(self):
        Cart.objects.filter(user=self.user).delete()
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de productos en el carrito sin token
    def test_product_cart_list_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)