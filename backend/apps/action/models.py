from datetime import date

from djmoney.models.fields import MoneyField
from djmoney.models.managers import money_manager
from model_utils.managers import InheritanceManager

from django.contrib.auth import get_user_model
from django.db import models

from apps.wallet.models import Wallet
from .manages import IncomesManager, ExpensesManager


class Category(models.Model):
    """
    Abstract base classes are useful when you want 
    to put some common information into a number of other models.
    """
    name = models.CharField(verbose_name='Category',
                            max_length=100)
    # logo = models.CharField('an id of icon')

    class Meta:
        abstract = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'


class IncomeCategory(Category):
    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='income_categories'
                             )

    class Meta:
        verbose_name = 'Income Category'
        verbose_name_plural = 'Income Categories'


class ExpenseCategory(Category):
    user = models.ForeignKey(get_user_model(),
                             verbose_name='User',
                             on_delete=models.CASCADE,
                             related_name='expense_categories'
                             )

    class Meta:
        verbose_name = 'Expense Category'
        verbose_name_plural = 'Expense Categories'


class Action(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=250,
                            blank=True)
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             related_name='actions')
    wallet = models.ForeignKey(Wallet,
                               verbose_name='To wallet',
                               on_delete=models.CASCADE,
                               related_name='actions')
    date = models.DateField(verbose_name='Date',
                            default=date.today)
    amount = MoneyField(verbose_name='Amount',
                        max_digits=10,
                        decimal_places=2,
                        default_currency='EUR')
    is_transaction = models.BooleanField(verbose_name='Is transaction?',
                                         default=False)

    objects = InheritanceManager()
    incomes = IncomesManager()
    expenses = ExpensesManager()

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    class Meta:
        ordering = ['-date', 'name']

        verbose_name = 'Action'
        verbose_name_plural = 'Actions'


class Income(Action):
    category = models.ForeignKey(ExpenseCategory,
                                 verbose_name='Category',
                                 on_delete=models.CASCADE,
                                 related_name='incomes')
    # організувати звязок між двома об'єктами транзації,
    # щоб при редагувані, видаленні це було в одному місці
    # transaction_rel = models.OneToOneField('Expense',
    #                                        verbose_name='Transaction',
    #                                        on_delete=models.CASCADE,
    #                                        blank=True,
    #                                        null=True)


class Expense(Action):
    category = models.ForeignKey(IncomeCategory,
                                 verbose_name='Category',
                                 on_delete=models.CASCADE,
                                 related_name='expenses')
