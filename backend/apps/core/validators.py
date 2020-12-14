from moneyed.classes import get_currency, CurrencyDoesNotExist
from rest_framework import serializers


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
