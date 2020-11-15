from moneyed.classes import get_currency, CurrencyDoesNotExist
# from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers

from .models import Wallet


class CurrencyCodeValidator:
    """
    Validator to check if this currency exists
    """

    def __call__(self, value):
        try:
            # try to find currency with this code
            get_currency(code=value)
        except CurrencyDoesNotExist as e:
            raise serializers.ValidationError(str(e))


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
