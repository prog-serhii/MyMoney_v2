from datetime import date
from djmoney.models.fields import MoneyField

from django.contrib.auth import get_user_model
from django.db import models

from apps.wallet.models import Wallet


class IncomeCategory(models.Model):
    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='income_categories'
                             )
    name = models.CharField(verbose_name='Name',
                            max_length=100)

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    class Meta:
        verbose_name = 'Income category'
        verbose_name_plural = 'Income categories'


class Income(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=250,
                            blank=True)
    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='incomes')
    category = models.ForeignKey(IncomeCategory,
                                 verbose_name='Category',
                                 on_delete=models.CASCADE,
                                 related_name='incomes')
    to_wallet = models.ForeignKey(Wallet,
                                  verbose_name='To wallet',
                                  on_delete=models.CASCADE,
                                  related_name='incomes')
    date = models.DateField(verbose_name='Date',
                            default=date.today)
    amount = MoneyField(verbose_name='Amount',
                        max_digits=10,
                        decimal_places=2,
                        default_currency='EUR')

    # objects = ExpenseManager()

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'
