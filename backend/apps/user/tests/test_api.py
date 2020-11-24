import base64
import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model


PASSWORD = 'pAssw0rd!'

CREATE_USER_URL = reverse('user:sign_up')
TOKEN_URL = reverse('user:token_create')


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(APITestCase):
    def test_user_can_sign_up(self):
        """Test creating using with a valid payload is successful"""
        payload = {
            'email': 'test@email.ua',
            'name': 'Test User',
            'password1': PASSWORD,
            'password2': PASSWORD
        }
        res = self.client.post(CREATE_USER_URL, payload)

        user = get_user_model().objects.last()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['id'], user.id)
        self.assertEqual(res.data['email'], user.email)
        self.assertEqual(res.data['name'], user.name)
        self.assertTrue(
            user.check_password(payload['password1'])
        )
        passwords = ['password', 'password1', 'password2']
        self.assertNotIn(res.data, passwords)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            'email': 'test@email.ua',
            'name': 'Test User',
            'password': PASSWORD
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_passwords_doesnt_match(self):
        payload = {
            'email': 'test@email.ua',
            'name': 'Test User',
            'password1': PASSWORD,
            'password2': 'invalid password'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@email.ua', 'password': PASSWORD}
        user = create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIsNotNone(res.data['access'])

        # Parse payload data from access token.
        access = res.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)

        self.assertIsNotNone(res.data['refresh'])
        self.assertEqual(payload_data['id'], user.id)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        create_user(email='test@londonappdev.com', password=PASSWORD)
        payload = {'email': 'test@londonappdev.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_no_user(self):
        """Test that token is not created if user doens't exist"""
        payload = {'email': 'test@londonappdev.com', 'password': PASSWORD}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})

        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
