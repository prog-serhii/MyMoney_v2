from rest_framework import serializers

from apps.core.validators import CurrencyCodeValidator
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    # ДОДАТИ ДОЗВІЛ ТІЛЬКИ ДЛЯ АВТОРИЗОВАНИХ
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    initial_balance_currency = serializers.CharField(
        required=True, write_only=True, validators=[CurrencyCodeValidator()])

    class Meta:
        model = Wallet
        exclude = ['id', 'created', 'updated']

        # extra_kwargs = {
        #     'initial_balance':
        #     {
        #         'write_only': True
        #     },
        # }
