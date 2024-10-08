from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from .models import User


# Tests para el registro de usuario
class RegisterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register')
        User.objects.create(
            username='TestExistingUsername',
            email='testexisting@email.com',
            password='TestPassword'
        )
        self.data = {
            'username': 'TestUsername',
            'email': 'test@email.com',
            'password': 'TestPassword',
        }


    # Prueba de registro exitoso
    def test_register_successful(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de registro con datos inválidos
    def test_register_invalid_data(self):
        del self.data['email']
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de registro con nombre de usuario existente
    def test_register_existing_username(self):
        self.data['username'] = 'TestExistingUsername'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de registro con correo electrónico existente
    def test_register_existing_email(self):
        self.data['email'] = 'testexisting@email.com'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


# Tests para el inicio de sesión
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')
        user = User.objects.create(
            username='TestUsername',
            email='test@email.com'
        )
        user.set_password('TestPassword')
        user.save()
        self.data = {
            'email': 'test@email.com',
            'password': 'TestPassword'
        }


    # Prueba de inicio de sesión exitoso
    def test_login_successful(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de inicio de sesión con correo electrónico inválido
    def test_login_invalid_email(self):
        self.data['email'] = 'incorrect@email.com'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de inicio de sesión con contraseña incorrecta
    def test_login_invalid_password(self):
        self.data['password'] = 'IncorrectPassword'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)
