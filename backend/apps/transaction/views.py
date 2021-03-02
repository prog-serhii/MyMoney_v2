from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter


from apps.api.mixins import ApiErrorsMixin
from .models import Income, Expense
from . import serializers
from . import services


class LargeResultsSetPagination(LimitOffsetPagination):
    default_limit = 50


class IncomeFilter(FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Income
        fields = ('account', 'category')


class ExpenseFilter(FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Expense
        fields = ('account', 'category')


class IncomeCategoryListAPI(ApiErrorsMixin, ListCreateAPIView):
    serializer_class = serializers.IncomeCategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_income_categories_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_income_category(user, serializer.validated_data)


class IncomeCategoryDetailAPI(ApiErrorsMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.IncomeCategorySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services. get_income_categories_by_user(user_id)

    def perform_destroy(self, instance):
        services.remove_income_category(instance)


class ExpenseCategoryListAPI(ApiErrorsMixin, ListCreateAPIView):
    serializer_class = serializers.ExpenseCategorySerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)

    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expense_categories_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_expense_category(user, serializer.validated_data)


class ExpenseCategoryDetailAPI(ApiErrorsMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ExpenseCategorySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expense_categories_by_user(user_id)

    def perform_destroy(self, instance):
        services.remove_expense_category(instance)


class IncomeListAPI(ApiErrorsMixin, ListCreateAPIView):
    serializer_class = serializers.IncomeListSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)

    search_fields = ('name',)
    ordering_fields = ('date', 'name',)
    filterset_class = IncomeFilter

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_incomes_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_income(user, serializer.validated_data)


class IncomeDetailAPI(ApiErrorsMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.IncomeDetailSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_incomes_by_user(user_id)

    def perform_update(self, serializer):
        income = self.get_object()
        services.update_income(income, serializer)

    def perform_destroy(self, instance):
        services.remove_income(instance)


class IncomeStatisticAPI(ApiErrorsMixin, APIView):
    filter_backend = DjangoFilterBackend
    filterset_class = IncomeFilter

    def filter_queryset(self, queryset):
        queryset = self.filter_backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_incomes_by_user(user_id)

    def get(self, request):
        incomes = self.filter_queryset(self.get_queryset())
        print(incomes)

        return Response('incomes.count()')


class ExpenseListAPI(ApiErrorsMixin, ListCreateAPIView):
    serializer_class = serializers.ExpenseListSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)

    search_fields = ('name',)
    ordering_fields = ('date', 'name')
    filterset_class = ExpenseFilter

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expenses_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_expense(user, serializer.validated_data)


class ExpenseDetailAPI(ApiErrorsMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ExpenseDetailSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_expenses_by_user(user_id)

    def perform_update(self, serializer):
        expense = self.get_object()
        services.update_expense(expense, serializer)

    def perform_destroy(self, instance):
        services.remove_expense(instance)


class TransferRemoveAPI(ApiErrorsMixin, DestroyAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_transfer_by_user(user_id)

    def perform_destroy(self, instance):
        services.remove_transfer(instance)


class TransferCreateAPI(ApiErrorsMixin, CreateAPIView):
    serializer_class = serializers.TransferCreateSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_transfer_by_user(user_id)

    def perform_create(self, serializer):
        user = self.request.user
        services.create_transfer(user, serializer.validated_data)
