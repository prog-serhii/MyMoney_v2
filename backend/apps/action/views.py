from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from . import serializers
from . import services


class SmallResultSetPagination(LimitOffsetPagination):
    default_limit = 10


class LargeResultsSetPagination(LimitOffsetPagination):
    default_limit = 50


class WalletActionListAPI(ListAPIView):
    serializer_class = serializers.WalletActionListSerializer
    pagination_class = SmallResultSetPagination
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name', )
    ordering_fields = ('date', 'name')

    def get_queryset(self):
        wallet_id = self.kwargs['wallet']
        return services.get_actions_by_wallet(wallet_id)


class WalletIncomeListAPI(ListAPIView):
    serializer_class = serializers.WalletIncomeListSerializer
    pagination_class = SmallResultSetPagination
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name', )
    ordering_fields = ('date', 'name')

    def get_queryset(self):
        wallet_id = self.kwargs['wallet']
        return services.get_incomes_by_wallet(wallet_id)


class WalletExpenseListAPI(ListAPIView):
    serializer_class = serializers.WalletExpenseListSerializer
    pagination_class = SmallResultSetPagination
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name', )
    ordering_fields = ('date', 'name')

    def get_queryset(self):
        wallet_id = self.kwargs['wallet']
        return services.get_expenses_by_wallet(wallet_id)


class IncomeListAPI(ListCreateAPIView):
    serializer_class = serializers.IncomeListSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name', )
    ordering_fields = ('date', 'name')

    def get_queryset(self):
        user = self.request.user
        return services.get_incomes_by_user(user)


class ExpenseListAPI(ListCreateAPIView):
    serializer_class = serializers.ExpenseListSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name', )
    ordering_fields = ('date', 'name')

    def get_queryset(self):
        user = self.request.user
        return services.get_expenses_by_user(user)
