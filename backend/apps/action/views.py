from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from . import serializers
from . import services


class LargeResultsSetPagination(LimitOffsetPagination):
    default_limit = 50


class IncomeCategoryListAPI(ListCreateAPIView):
    serializer_class = serializers.IncomeCategorySerializer
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_income_categories_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_income_category(user, serializer.validated_data)


class IncomeCategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.IncomeCategorySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_income_categories_by_user(user_id)

    def perform_update(self, serializer):
        pass

    def perform_destroy(self, instance):
        services.remove_income_category(instance)


class ExpenseCategoryListAPI(ListCreateAPIView):
    serializer_class = serializers.ExpenseCategorySerializer
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expense_categories_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_expense_category(user, serializer.validated_data)


class ExpenseCategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ExpenseCategorySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expense_categories_by_user(user_id)

    def perform_update(self, serializer):
        pass

    def perform_destroy(self, instance):
        services.remove_expense_category(instance)


class IncomeListAPI(ListCreateAPIView):
    serializer_class = serializers.IncomeListSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)

    search_fields = ('name',)
    ordering_fields = ('date', 'name',)
    filterset_fields = ('wallet', 'category')

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_incomes_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_income(user, serializer.validated_data)


class IncomeDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.IncomeDetailSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_incomes_by_user(user_id)


class ExpenseListAPI(ListCreateAPIView):
    serializer_class = serializers.ExpenseListSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)

    search_fields = ('name',)
    ordering_fields = ('date', 'name')
    filterset_fields = ('wallet', 'category')

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expenses_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_expense(user, serializer.validated_data)


class ExpenseDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ExpenseDetailSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expenses_by_user(user_id)
