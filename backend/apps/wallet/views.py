from django.contrib.auth.models import User

from rest_framework import generics

from .models import Wallet
from .serializers import WalletSerializer


class WalletListCreateView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
