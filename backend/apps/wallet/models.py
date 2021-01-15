import uuid

from djmoney.money import Money
from djmoney.models.fields import MoneyField
from djmoney.models.managers import money_manager

from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model

from apps.wallet.managers import WalletManager


class Wallet(models.Model):

    class TypeOfWallet(models.TextChoices):
        CASHE = 'cashe', 'Cashe'
        CARD = 'card', 'Bank Card'

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    initial_balance = MoneyField(verbose_name='Initial balance',
                                 max_digits=10,
                                 decimal_places=2,
                                 default=0,
                                 default_currency='EUR',
                                 blank=False,
                                 null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # Django-money leaves you to use any custom model managers you like for your models,
    # but it needs to wrap some of the methods to allow searching for models with money values.
    objects = money_manager(WalletManager())

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'
        ordering = ['updated']

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    @property
    def currency(self) -> str:
        """
        Return currency of the wallet
        """
        return str(self.initial_balance.currency)

    @property
    def balance(self) -> Money:
        """
        Return Money object - total balance
        """
        # initial_balance = self.initial_balance

        # def aggregate_sum(instance, currency) -> Money:
        #     amount = instance.aggregate(Sum('amount'))['amount__sum']

        #     if amount is None:
        #         amount = float()
        #     else:
        #         amount = float(amount)

        #     return Money(amount, self.currency)

        # incomes = aggregate_sum(self.incomes, self.currency)
        # expenses = aggregate_sum(self.expenses, self.currency)

        # balance = initial_balance + incomes - expenses

        # return round(balance, 2)

        return round(self.initial_balance, 2)
