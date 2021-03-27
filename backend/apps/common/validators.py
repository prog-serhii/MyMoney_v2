from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# 1. один і той же користувач між
# * витрата + рахунок
# * прибуток + рахунок

# 2. одна і та ж валюта між
# * витрата + рахунок
# * прибуток + рахунок

# def clean(self):
#     if self.balance_currency != self.initial_balance_currency:
#         raise ValidationError(_('Currencies of balance and initial_balance must be the same.'))

# def save(self, *args, **kwargs):
#     self.full_clean()
#     return super().save(*args, **kwargs)


def check_transaction_currencies(first_currency, second_currency):
    if first_currency != second_currency:
        raise ValidationError(
            _('CURENCY')
        )


def check_account_currencies(balance_currency, initial_balance_currency):
    if balance_currency != initial_balance_currency:
        raise ValidationError(
            _('Currencies of balance and initial balance must be the same.')
        )


def check_transaction_users(first_user, second_user):
    if first_user != second_user:
        raise ValidationError('USRS')
