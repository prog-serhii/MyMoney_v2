from djmoney.models.fields import CurrencyField
# from djmoney.contrib.exchange.models import get_rate
# from moneyed.classes import get_currency, CurrencyDoesNotExist

from django.db import models
# from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


# def currency_code_validator(value):
#     try:
#         # try to find currency with this code
#         get_currency(code=value)
#     except CurrencyDoesNotExist as e:
#         raise ValidationError(
#             str(e),
#             params={'value': value}
#         )


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    main_currency = CurrencyField(verbose_name='Main currency')
    # validators=[currency_code_validator])
    currencies = ArrayField(
        CurrencyField(blank=True, null=True),
        # validators=[currency_code_validator]),
        size=5,
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    # def user_currencies(self):
    #     currencies = []

    #     for currency in self.currencies:
    #         name = get_currency(currency).name
    #         rate = round(get_rate(currency, self.main_currency), 4)
    #         main = True if currency == self.main_currency else False

    #         currencies.append(
    #             {
    #                 'code': currency,
    #                 'name': name,
    #                 'rate': rate,
    #                 'main': main
    #             }
    #         )

    #     return currencies
