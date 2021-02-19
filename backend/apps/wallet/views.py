from djmoney.contrib.exchange.exceptions import MissingRate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.utils.translation import gettext as _

from . import services
from . import serializers


class AuthMixin:
    """
    Apply this mixin to any view get queryset of wallets
    where the owner is the currently authenticated user.
    """

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_wallets_by_user(user_id)


class WalletListAPI(AuthMixin, ListCreateAPIView):
    pagination_class = None

    def get_serializer_class(self, *args, **kwargs):
        request_method = self.request.method
        if request_method == 'GET':
            return serializers.WalletListSerializer
        # POST request
        else:
            return serializers.WalletDetailSerializer

    def perform_create(self, serializer):
        user = self.request.user
        services.create_wallet(user, serializer.validated_data)


class WalletDetailAPI(AuthMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WalletDetailSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        services.update_wallet(instance, serializer)

    def perform_destroy(self, instance):
        services.remove_wallet(instance)


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
            amount = services.get_total_balance_of(wallets, currency)

            response = {
                'amount': amount,
                'currency': currency
            }

            return Response(response, status=HTTP_200_OK)

        except MissingRate:
            response = {
                'error': _("Rate for '{}' does not exist.").format(currency)
            }

            return Response(response, status=HTTP_400_BAD_REQUEST)


# class WalletStatisticAPI(AuthMixin, APIView):
#     """
#     1. filter by date range
#     2. aggregate sum of incomes
#     3. aggregate sum of expenses
#     4.
#     """

#     def get(self, request, format=None):
#         incomes = services.filter_by_date_range()
#         expenses = services.filter_by_date_range()

#         sum_of_incomes = services.get_sum_of(incomes)
#         sum_of_expenses = services.get_sum_of(expenses)
