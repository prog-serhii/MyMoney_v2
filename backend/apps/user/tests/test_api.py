import base64
import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model


PASSWORD = 'pAssw0rd!'


def create_user(username='test@email.ua', password=PASSWORD):  # new
    return get_user_model().objects.create_user(
        email=username,
        name='Test User',
        password=password
    )


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        url = reverse('sign_up')
        res = self.client.post(url, data={
            'email': 'test@email.ua',
            'name': 'Test User',
            'password1': PASSWORD,
            'password2': PASSWORD
        })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertEqual(res.data['id'], user.id)
        self.assertEqual(res.data['email'], user.email)
        self.assertEqual(res.data['name'], user.name)

    def test_user_can_log_in(self):
        user = create_user()
        res = self.client.post(reverse('log_in'), data={
            'email': user.email,
            'password': PASSWORD,
        })

        # Parse payload data from access token.
        access = response.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertIsNotNone(res.data['refresh'])
        self.assertEqual(payload_data['id'], user.id)
        self.assertEqual(payload_data['email'], user.email)
        self.assertEqual(payload_data['name'], user.name)
