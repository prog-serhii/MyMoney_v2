from rest_framework import serializers

from .models import Wallet


class WalletRepresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('id', 'name')


class WalletListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('id', 'name', 'icon', 'formatted_balance', 'currency')


class WalletDetailSerializer(serializers.ModelSerializer):
    initial_balance_currency = serializers.CharField(write_only=True)

    class Meta:
        model = Wallet
        fields = ('id', 'name', 'icon', 'balance', 'initial_balance',
                  'initial_balance_currency', 'currency', 'created')
        read_only_fields = ('id', 'balance')
