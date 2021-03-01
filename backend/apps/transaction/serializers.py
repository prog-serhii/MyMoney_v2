from datetime import date
from rest_framework import serializers

from apps.account.serializers import AccountRepresentationSerializer
from apps.account.models import Account
from .models import Income, Expense, Transfer, IncomeCategory, ExpenseCategory


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


class TransferCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,
                                 allow_blank=False,
                                 max_length=250)
    date = serializers.DateField(default=date.today)
    income_amount = serializers.DecimalField(required=True,
                                             max_digits=10,
                                             decimal_places=2)
    income_currency = serializers.CharField(required=True,
                                            allow_blank=False,
                                            max_length=5)
    income_account = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all())
    income_category = serializers.PrimaryKeyRelatedField(
        queryset=IncomeCategory.objects.all())
    expense_amount = serializers.DecimalField(required=True,
                                              max_digits=10,
                                              decimal_places=2)
    expense_currency = serializers.CharField()
    expense_account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    expense_category = serializers.PrimaryKeyRelatedField(
        queryset=ExpenseCategory.objects.all())
    rate = serializers.DecimalField(required=True,
                                    max_digits=10,
                                    decimal_places=2)


class TransferDetailSerializer(serializers.ModelSerializer):
    income = IncomeDetailSerializer()
    expense = ExpenseDetailSerializer()

    class Meta:
        model = Transfer
        fields = ('income', 'expense', 'rate')
