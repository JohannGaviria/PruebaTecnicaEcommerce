from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from .models import Product


# Tests para obtener una lista de los productos
class ProductListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('product_list')
        # Crea algunos productos para las pruebas
        for i in range(15):
            Product.objects.create(name=f'Product {i}', price=i * 10, availability=i*2)


    # Prueba de obtener lista de producto exitosamente
    def test_product_list_success(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)
