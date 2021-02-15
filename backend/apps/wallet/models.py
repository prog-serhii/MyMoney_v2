from datetime import date

from djmoney.models.fields import MoneyField

from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class Wallet(models.Model):

    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='wallets',
                             blank=False,
                             null=False)
    name = models.CharField(verbose_name='Name',
                            max_length=50,
                            blank=False,
                            null=False)
    icon = models.CharField(verbose_name='Icon of wallet',
                            max_length=20,
                            default='',
                            blank=False,
                            null=False)
    initial_balance = MoneyField(verbose_name='Initial balance',
                                 max_digits=10,
                                 decimal_places=2,
                                 default=0,
                                 default_currency='EUR',
                                 blank=False,
                                 null=False)
    balance = MoneyField(verbose_name='Total balance',
                         max_digits=10,
                         decimal_places=2,
                         default=0,
                         default_currency='EUR',
                         blank=False,
                         null=False)
    created = models.DateField(verbose_name='Date of initial balance',
                               default=date.today,
                               blank=False,
                               null=False)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'
        ordering = ('-name',)

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    def clean(self):
        if self.balance_currency != self.initial_balance_currency:
            raise ValidationError('Currencies of balance and initial_balance must be the same.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    @property
    def currency(self) -> str:
        """
        Return currency of the wallet
        """
        return str(self.balance.currency)

    @property
    def formatted_balance(self) -> str:
        """
        Return formatted balance of the wallet
        """
        return str(self.balance)
