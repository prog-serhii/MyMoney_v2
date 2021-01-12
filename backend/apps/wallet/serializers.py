from rest_framework import serializers

from apps.core.validators import CurrencyCodeValidator
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    """
    Base class for wallet's serializers
    """
    balance = serializers.SerializerMethodField()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    initial_balance_currency = serializers.CharField(
        required=True, validators=[CurrencyCodeValidator()])

    def get_balance(self, obj):
        return obj.balance.amount


class WalletListSerializer(WalletSerializer):

    class Meta:
        model = Wallet
        fields = ('uid', 'name', 'balance', 'currency')


class CreateWalletSerializer(WalletSerializer):

    class Meta:
        model = Wallet
        fields = ('user', 'name', 'wallet_type', 'initial_balance', 'initial_balance_currency')


class WalletDetailSerializer(WalletSerializer):
    class Meta:
        model = Wallet
        exclude = ('uid',)
