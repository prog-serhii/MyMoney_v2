from datetime import date
from djmoney.models.fields import MoneyField

from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from apps.wallet.models import Wallet


class Category(models.Model):
    """
    Abstract base class to put some common 
    information into some 'Category' models.
    """
    name = models.CharField(verbose_name='Category',
                            max_length=100)

    class Meta:
        abstract = True

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
    """
    Abstract base class to put some common 
    information into some 'Action' models.
    """
    name = models.CharField(verbose_name='Name',
                            max_length=250,
                            blank=True)
    date = models.DateField(verbose_name='Date',
                            default=date.today)
    amount = MoneyField(verbose_name='Amount',
                        max_digits=10,
                        decimal_places=2,
                        default=0,
                        default_currency='EUR',
                        blank=False,
                        null=False)
    is_transaction = models.BooleanField(verbose_name='Is transaction?',
                                         default=False)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Income(Action):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             related_name='incomes')
    wallet = models.ForeignKey(Wallet,
                               verbose_name='To wallet',
                               on_delete=models.CASCADE,
                               related_name='incomes')
    category = models.ForeignKey(IncomeCategory,
                                 verbose_name='Category',
                                 on_delete=models.CASCADE,
                                 related_name='incomes')


class Expense(Action):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             related_name='expenses')
    wallet = models.ForeignKey(Wallet,
                               verbose_name='To wallet',
                               on_delete=models.CASCADE,
                               related_name='expenses')
    category = models.ForeignKey(ExpenseCategory,
                                 verbose_name='Category',
                                 on_delete=models.CASCADE,
                                 related_name='expenses')
    related_income = models.OneToOneField('Income',
                                          verbose_name='Related Income',
                                          related_name='related_expense',
                                          on_delete=models.SET_NULL,
                                          blank=True,
                                          null=True)

    def clean(self):
        if self.is_transaction != bool(self.related_income):
            raise ValidationError(
                'If field \'is_transaction\' is True then field \'related_income\' \
                must contain a reference to the associated object. And vice versa.',
                code='invalid')
