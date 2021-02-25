from rest_framework import serializers

from apps.account.serializers import AccountRepresentationSerializer
from .models import Income, Expense, IncomeCategory, ExpenseCategory


class IncomeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeCategory
        fields = ('id', 'name')


class ExpenseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseCategory
        fields = ('id', 'name')


class IncomeListSerializer(serializers.ModelSerializer):
    amount_currency = serializers.CharField(write_only=True)

    class Meta:
        model = Income
        fields = ('id', 'name', 'amount', 'formatted_amount', 'currency',
                  'date', 'is_transfer', 'account', 'category', 'amount_currency')
        read_only_fields = ('id',)

        extra_kwargs = {
            'amount': {'write_only': True},
            'category': {'write_only': True},
            'account': {'write_only': True}
        }


class IncomeDetailSerializer(serializers.ModelSerializer):
    account = AccountRepresentationSerializer(read_only=True)
    category = IncomeCategorySerializer(read_only=True)

    class Meta:
        model = Income
        fields = ('id', 'name', 'account', 'amount', 'amount_currency',
                  'date', 'category', 'is_transfer')


class ExpenseListSerializer(serializers.ModelSerializer):
    amount_currency = serializers.CharField(write_only=True)

    class Meta:
        model = Expense
        fields = ('id', 'name', 'amount', 'formatted_amount', 'currency',
                  'date', 'is_transfer', 'account', 'category', 'amount_currency')
        read_only_fields = ('id',)

        extra_kwargs = {
            'amount': {'write_only': True},
            'category': {'write_only': True},
            'account': {'write_only': True}
        }


class ExpenseDetailSerializer(serializers.ModelSerializer):
    account = AccountRepresentationSerializer(read_only=True)
    category = ExpenseCategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ('id', 'name', 'account', 'amount', 'amount_currency',
                  'date', 'category', 'is_transfer')
