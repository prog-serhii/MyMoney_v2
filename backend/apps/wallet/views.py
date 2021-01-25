from djmoney.contrib.exchange.exceptions import MissingRate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Wallet
from . import services
from . import serializers


class AuthMixin:
    """
    Apply this mixin to any view get queryset of wallets
    where the owner is the currently authenticated user.
    """
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return services.get_wallets_by(user)


class WalletListAPI(AuthMixin, ListCreateAPIView):
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'initial_balance_currency')
    ordering_fields = ('name', 'initial_balance_currency')

    def get_serializer_class(self, *args, **kwargs):
        request_method = self.request.method
        if request_method == 'GET':
            return serializers.WalletListSerializer
        else:
            return serializers.WalletCreateUpdateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        services.create_wallet({'user': user, **serializer.data})


class WalletDetailAPI(AuthMixin, RetrieveUpdateDestroyAPIView):

    def get_serializer_class(self, *args, **kwargs):
        request_method = self.request.method
        if request_method == 'GET':
            return serializers.WalletDetailSerializer
        else:
            return serializers.WalletCreateUpdateSerializer

    # def perform_update(self, serializer):
    #     services.update_wallet(serializer.data)

    # def perform_destroy(self, instance):
    #     services.delete_wallet(instance)


class WalletTotalBalanceAPI(AuthMixin, APIView):
    """
    Return a total balance of all user's wallets in a curtain currency
    """

    def get(self, request, format=None):
        wallets = self.get_queryset()

        try:
            currency = self.request.query_params['currency']
        except KeyError:
            currency = self.request.user.main_currency

        try:
            balance = services.get_total_balance_of(wallets, currency)

            response = {
                'balance': balance,
                'currency': currency
            }

            return Response(response, status=HTTP_200_OK)

        except MissingRate:
            response = {
                'message': 'Error',
                'error': 'This currency does not exist'
            }

            return Response(response, status=HTTP_400_BAD_REQUEST)


class WalletStatisticAPI(AuthMixin, APIView):
    """
    1. filter by date range
    2. aggregate sum of incomes
    3. aggregate sum of expenses
    4. 
    """

    def get(self, request, format=None):
        incomes = services.filter_by_date_range()
        expenses = services.filter_by_date_range()

        sum_of_incomes = services.get_sum_of(incomes)
        sum_of_expenses = services.get_sum_of(expenses)
