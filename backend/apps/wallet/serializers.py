from djmoney.serializers import MoneyField

from rest_framework import serializers

from .models import Wallet


class WalletListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('pk', 'name', 'balance', 'currency')


class WalletCreateUpdateSerializer(serializers.ModelSerializer):
    initial_balance_currency = serializers.CharField()

    class Meta:
        model = Wallet
        fields = ('name', 'wallet_type', 'initial_balance',
                  'initial_balance_currency')


class WalletDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('pk', 'name', 'wallet_type', 'balance',
                  'currency', 'initial_balance', 'created', 'updated')
