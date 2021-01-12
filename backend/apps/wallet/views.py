from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from .models import Wallet
from .serializers import (
    WalletListSerializer, CreateWalletSerializer, WalletDetailSerializer
)


class SmallResultSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10


class WalletsForCurentUserMixin:
    """
    Apply this mixin to any view or viewset to get queryset
    of wallets where owner is the current user.
    """

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)


class WalletListView(WalletsForCurentUserMixin, ListAPIView):
    """
    This view should return a list of all the wallets
    for the currently authenticated user.
    """
    serializer_class = WalletListSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = SmallResultSetPagination


class CreateWalletView(WalletsForCurentUserMixin, CreateAPIView):
    serializer_class = CreateWalletSerializer
    permission_classes = (IsAuthenticated, )


class WalletDetailView(WalletsForCurentUserMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = WalletDetailSerializer
    permission_classes = (IsAuthenticated, )
