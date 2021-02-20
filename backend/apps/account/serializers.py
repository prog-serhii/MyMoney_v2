from rest_framework import serializers

from .models import Account


class AccountRepresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'name')


class AccountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'name', 'icon', 'formatted_balance', 'currency')


class AccountDetailSerializer(serializers.ModelSerializer):
    initial_balance_currency = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('id', 'name', 'icon', 'balance', 'initial_balance',
                  'initial_balance_currency', 'created')
        read_only_fields = ('id', 'balance')
