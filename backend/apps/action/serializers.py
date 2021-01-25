from rest_framework import serializers

from apps.wallet.models import Wallet
from apps.wallet.serializers import WalletRepresentationSerializer
from .models import Action, Income, Expense


class IncomeCategoryRepresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('pk', 'name')


class ExpenseRepresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('pk', 'name')


class WalletActionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ('name', 'amount', 'amount_currency', 'date',
                  'is_transaction', 'is_income', 'is_expense')


class WalletIncomeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ('name', 'amount', 'amount_currency', 'date',
                  'is_transaction', 'is_income', 'is_expense')


class WalletExpenseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('name', 'amount', 'amount_currency', 'date',
                  'is_transaction', 'is_income', 'is_expense')


class IncomeListSerializer(serializers.ModelSerializer):
    wallet = WalletRepresentationSerializer(read_only=True)
    category = IncomeCategoryRepresentationSerializer(read_only=True)

    class Meta:
        model = Income
        fields = ('name', 'wallet', 'amount',
                  'date', 'category', 'is_transaction')


class ExpenseListSerializer(serializers.ModelSerializer):
    wallet = WalletRepresentationSerializer(read_only=True)
    category = ExpenseRepresentationSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ('name', 'wallet', 'amount',
                  'date', 'category', 'is_transaction')
