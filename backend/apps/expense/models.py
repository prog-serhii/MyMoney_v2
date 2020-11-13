from djmoney.models.fields import MoneyField

from django.contrib.auth import get_user_model
from django.db import models

from apps.wallet.models import Wallet


class ExpenseCategory(models.Model):
    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='expense_categories'
                             )
    name = models.CharField(verbose_name='Name',
                            max_length=100)

    def __str__(self):
        return f"{self.name} ({str(self.user)})"

    class Meta:
        verbose_name = 'Expense category'
        verbose_name_plural = 'Expense categories'


class Expense(models.Model):
    title = models.CharField(verbose_name='Title',
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
    wallet = models.ForeignKey(Wallet,
                               verbose_name='Wallet',
                               on_delete=models.CASCADE,
                               related_name='expenses')
    data = models.DateField(verbose_name='Data',
                            auto_now_add=True)
    amount = MoneyField(verbose_name='Amount',
                        max_digits=10,
                        decimal_places=2,
                        default_currency='EUR')

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
