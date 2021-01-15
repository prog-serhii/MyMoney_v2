from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Wallet
from .serializers import (
    WalletListSerializer, WalletCreateSerializer, WalletDetailSerializer
)


class WalletsForCurentUserMixin:
    """
    Apply this mixin to any view or viewset to get queryset
    of wallets where owner is the currently authenticated user.
    """
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)


class WalletListView(WalletsForCurentUserMixin, ListCreateAPIView):
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'initial_balance_currency')
    ordering_fields = ('name', 'initial_balance_currency')

    def get_serializer_class(self):
        """
        Returns the different serializers that should be used
        for read and write (POST request) operations. 
        """
        if self.request.method == 'POST':
            return WalletCreateSerializer
        return WalletListSerializer


class WalletDetailView(WalletsForCurentUserMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = WalletDetailSerializer
