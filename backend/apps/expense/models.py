from datetime import date
from djmoney.models.fields import MoneyField

from django.contrib.auth import get_user_model
from django.db import models

from apps.wallet.models import Wallet
from apps.expense.managers import ExpenseManager


class ExpenseCategory(models.Model):
    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='expense_categories'
                             )
    name = models.CharField(verbose_name='Name',
                            max_length=100)

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    class Meta:
        verbose_name = 'Expense category'
        verbose_name_plural = 'Expense categories'


class Expense(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=250,
                            blank=True)
    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='expenses')
    category = models.ForeignKey(ExpenseCategory,
                                 verbose_name='Category',
                                 on_delete=models.CASCADE,
                                 related_name='expenses')
    from_wallet = models.ForeignKey(Wallet,
                                    verbose_name='From wallet',
                                    on_delete=models.CASCADE,
                                    related_name='expenses')
    date = models.DateField(verbose_name='Date',
                            default=date.today)
    amount = MoneyField(verbose_name='Amount',
                        max_digits=10,
                        decimal_places=2,
                        default_currency='EUR')

    objects = ExpenseManager()

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
