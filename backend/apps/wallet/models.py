from djmoney.models.fields import MoneyField

from django.db import models
from django.contrib.auth import get_user_model

from .managers import WalletManager


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
    start_balance = MoneyField(verbose_name='Start balance',
                               max_digits=10,
                               decimal_places=2,
                               default=0,
                               default_currency='EUR',
                               blank=False,
                               null=False)
    logo = models.ImageField(verbose_name='Logo',
                             upload_to='logos/wallets/%Y/%m/%d/',
                             blank=True
                             )
    active = models.BooleanField(verbose_name='Active',
                                 default=True)

    objects = WalletManager()

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    def __str__(self):
        return f'{self.name}__{self.user}'

    @property
    def currency(self) -> str:
        return str(self.start_balance.currency)
