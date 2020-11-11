from djmoney.models.fields import MoneyField
from djmoney.models.managers import money_manager

from django.db import models
from django.contrib.auth import get_user_model

from .managers import WalletManager


class Wallet(models.Model):

    class TypeOfWallet(models.TextChoices):
        CASHE = 'cashe', 'Cashe'
        CARD = 'card', 'Bank Card'

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
    wallet_type = models.CharField(verbose_name='Type of wallet',
                                   max_length=10,
                                   choices=TypeOfWallet.choices,
                                   default=TypeOfWallet.CASHE)
    start_balance = MoneyField(verbose_name='Start balance',
                               max_digits=10,
                               decimal_places=2,
                               default=0,
                               default_currency='EUR',
                               blank=False,
                               null=False)
    # logo = models.ImageField(verbose_name='Logo',
    #                          upload_to='logos/wallets/%Y/%m/%d/',
    #                          blank=True
    #                          )
    active = models.BooleanField(verbose_name='Active',
                                 default=True)

    # Django-money leaves you to use any custom model managers you like for your models,
    # but it needs to wrap some of the methods to allow searching for models with money values.
    objects = money_manager(WalletManager())

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    def __str__(self) -> str:
        return f'{self.name}__{self.user}'

    @property
    def currency(self) -> str:
        """
        Return currency of the wallet
        """
        return str(self.start_balance.currency)
