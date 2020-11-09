from django.contrib.auth.models import User

from rest_framework import generics

from .models import Wallet
from .serializers import WalletSerializer


class WalletListCreateView(generics.ListCreateAPIView):
    # Mocking user
    user = User.objects.first()

    queryset = Wallet.objects.by_user(user)
    serializer_class = WalletSerializer
