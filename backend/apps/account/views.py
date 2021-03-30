import time

from djmoney.contrib.exchange.exceptions import MissingRate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.utils.translation import gettext as _

from apps.common.mixins import ApiErrorsMixin
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
        account_id = self.get_object().id
        services.update_account(account_id, serializer.validated_data)

    def perform_destroy(self, instance):
        services.remove_account(instance)


class AccountTotalBalanceAPI(AuthMixin, ApiErrorsMixin, APIView):
    """
    Return a total balance of all user's accounts in a curtain currency
    """

    def get(self, request, format=None):
        # simulation
        time.sleep(2)

        accounts = self.get_queryset()

        try:
            currency = self.request.query_params['currency']
        except KeyError:
            currency = self.request.user.main_currency

        try:
            amount = services.get_total_balance_of(accounts, currency)

            response = {
                'amount': amount.amount,
                'currency': currency
            }

            return Response(response, status=HTTP_200_OK)

        except MissingRate:
            # Переписати

            response = {
                'error': _("Rate for '{}' does not exist.").format(currency)
            }

            return Response(response, status=HTTP_400_BAD_REQUEST)


class CurrenciesAPI(ApiErrorsMixin, APIView):
    """
    """

    def get(self, request, format=None):
        ALL_CURRENCIES = 'all'
        USERS_CURRENCIES = 'user'
        DEFAULT_TYPE = USERS_CURRENCIES

        try:
            type_of_currencies = self.request.query_params['type']
        except KeyError:
            type_of_currencies = DEFAULT_TYPE

        if type_of_currencies == ALL_CURRENCIES:
            # get all available currencies
            currencies = services.get_available_currencies()
        elif type_of_currencies == USERS_CURRENCIES:
            # get currencies of user's accounts
            user_id = self.request.user.id
            currencies = services.get_currencies_by_user(user_id)
        else:
            raise ValueError(_('Not valid GET parameter - \'type\''))

        response = {
            'currencies': currencies
        }

        return Response(response, status=HTTP_200_OK)


class CurrencyRatesAPI(ApiErrorsMixin, APIView):
    """
    """

    def get(self, request, format=None):
        # simulation
        time.sleep(2)

        try:
            currency = self.request.query_params['currency']
        except KeyError:
            currency = self.request.user.main_currency

        user = self.request.user.id
        rates = services.get_exchange_rates(user, currency)

        response = {
            'rates': rates,
            'baseCurrency': currency
        }

        return Response(response, status=HTTP_200_OK)
