from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Wallet
        exclude = ['id', 'logo']
        extra_kwargs = {
            'start_balance': {'write_only': True},
        }

    # ДОДАТИ ВАЛІДАЦІЮ НА start_balance_currency
