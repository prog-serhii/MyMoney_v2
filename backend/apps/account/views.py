from djmoney.contrib.exchange.exceptions import MissingRate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.utils.translation import gettext as _

from apps.api.mixins import ApiErrorsMixin
from . import services
from . import serializers


class AuthMixin:
    """
    Apply this mixin to any view get queryset of accounts
    where the owner is the currently authenticated user.
    """

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_accounts_by_user(user_id)


class AccountListAPI(AuthMixin, ApiErrorsMixin, ListCreateAPIView):

    def get_serializer_class(self, *args, **kwargs):
        request_method = self.request.method
        if request_method == 'GET':
            return serializers.AccountListSerializer
        # POST request
        else:
            return serializers.AccountDetailSerializer

    def perform_create(self, serializer):
        user = self.request.user
        services.create_account(user, serializer.validated_data)


class AccountDetailAPI(AuthMixin, ApiErrorsMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AccountDetailSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        services.update_account(instance, serializer)

    def perform_destroy(self, instance):
        services.remove_account(instance)


class AccountTotalBalanceAPI(AuthMixin, ApiErrorsMixin, APIView):
    """
    Return a total balance of all user's accounts in a curtain currency
    """

    def get(self, request, format=None):
        accounts = self.get_queryset()

        try:
            currency = self.request.query_params['currency']
        except KeyError:
            currency = self.request.user.main_currency

        try:
            amount = services.get_total_balance_of(accounts, currency)

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
