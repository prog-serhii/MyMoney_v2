from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        url = reverse('sign_up')
        res = self.client.post(url, data={
            'email': 'test@email.ua',
            'name': 'Test User',
            'password1': 'pass123test',
            'password2': 'pass123test'
        })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertEqual(res.data['id'], user.id)
        self.assertEqual(res.data['email'], user.email)
        self.assertEqual(res.data['name'], user.name)
