from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse
from django.contrib.auth import get_user_model

from ..factories import WalletFactory


class WalletListAPITests(APITestCase):

    def setUp(self):
        name = 'bGhnssd'
        email = 'asddsff@dsgs.yu'
        password = 'tgdfsgdf@sdfwc.com'

        data = {
            'name': name,
            'email': email,
            'password': password
        }

        self.user = get_user_model().objects.create_user(**data)

        url = reverse('api-jwt-create')
        response = self.client.post(url, data, format='json')

        self.access_token = response.data['access']

    def test_wallet_list(self):
        WalletFactory.create_batch(
            7,
            user=self.user
        )

        url = reverse('api-wallets-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.access_token}')
        response = self.client.get(url, data={'format': 'json'})

        print()
        print(response)
        print()
