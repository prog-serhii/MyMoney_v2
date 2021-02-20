from rest_framework import serializers

from apps.wallet.serializers import WalletRepresentationSerializer
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
                  'date', 'is_transaction', 'wallet', 'category', 'amount_currency')
        read_only_fields = ('id',)

        extra_kwargs = {
            'amount': {'write_only': True},
            'category': {'write_only': True},
            'wallet': {'write_only': True}
        }


class IncomeDetailSerializer(serializers.ModelSerializer):
    wallet = WalletRepresentationSerializer(read_only=True)
    category = IncomeCategorySerializer(read_only=True)

    class Meta:
        model = Income
        fields = ('id', 'name', 'wallet', 'amount', 'amount_currency',
                  'date', 'category', 'is_transaction')


class ExpenseListSerializer(serializers.ModelSerializer):
    amount_currency = serializers.CharField(write_only=True)

    class Meta:
        model = Expense
        fields = ('id', 'name', 'amount', 'formatted_amount', 'currency',
                  'date', 'is_transaction', 'wallet', 'category', 'amount_currency')
        read_only_fields = ('id',)

        extra_kwargs = {
            'amount': {'write_only': True},
            'category': {'write_only': True},
            'wallet': {'write_only': True}
        }


class ExpenseDetailSerializer(serializers.ModelSerializer):
    wallet = WalletRepresentationSerializer(read_only=True)
    category = ExpenseCategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ('id', 'name', 'wallet', 'amount', 'amount_currency',
                  'date', 'category', 'is_transaction')
