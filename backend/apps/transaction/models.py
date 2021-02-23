from datetime import date
from djmoney.models.fields import MoneyField

from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.account.models import Account


class Category(models.Model):
    """
    Abstract base class for different 'Category' models.
    """
    name = models.CharField(verbose_name=_('Category'),
                            max_length=100)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'


class IncomeCategory(Category):
    user = models.ForeignKey(get_user_model(),
                             verbose_name=_('User'),
                             on_delete=models.CASCADE,
                             related_name='income_categories'
                             )

    class Meta:
        verbose_name = _('Income Category')
        verbose_name_plural = _('Income Categories')


class ExpenseCategory(Category):
    user = models.ForeignKey(get_user_model(),
                             verbose_name=_('User'),
                             on_delete=models.CASCADE,
                             related_name='expense_categories'
                             )

    class Meta:
        verbose_name = _('Expense Category')
        verbose_name_plural = _('Expense Categories')


class Transaction(models.Model):
    """
    Abstract base class for different 'Transaction' models.
    """
    name = models.CharField(verbose_name=_('Name'),
                            max_length=250,
                            blank=False,
                            null=False)
    date = models.DateField(verbose_name=_('Date'),
                            default=date.today)
    amount = MoneyField(verbose_name=_('Amount'),
                        max_digits=10,
                        decimal_places=2,
                        blank=False,
                        null=False)
    is_transaction = models.BooleanField(verbose_name=_('Is transaction?'),
                                         default=False)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    @property
    def currency(self) -> str:
        """
        Return currency of the transaction
        """
        return str(self.amount.currency)

    @property
    def formatted_amount(self) -> str:
        """
        Return formatted amount of the transaction
        """
        return str(self.amount)


class Income(Transaction):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name=_('User'),
                             related_name='incomes',
                             blank=False,
                             null=False)
    account = models.ForeignKey(Account,
                                verbose_name=_('To account'),
                                on_delete=models.CASCADE,
                                related_name='incomes',
                                blank=False,
                                null=False)
    category = models.ForeignKey(IncomeCategory,
                                 verbose_name=_('Category'),
                                 on_delete=models.CASCADE,
                                 related_name='incomes',
                                 blank=False,
                                 null=False)

    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')


class Expense(Transaction):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name=_('User'),
                             related_name='expenses',
                             blank=False,
                             null=False)
    account = models.ForeignKey(Account,
                                verbose_name=_('To account'),
                                on_delete=models.CASCADE,
                                related_name='expenses',
                                blank=False,
                                null=False)
    category = models.ForeignKey(ExpenseCategory,
                                 verbose_name=_('Category'),
                                 on_delete=models.CASCADE,
                                 related_name='expenses',
                                 blank=False,
                                 null=False)
    related_income = models.OneToOneField('Income',
                                          verbose_name=_('Related Income'),
                                          related_name='related_expense',
                                          on_delete=models.SET_NULL,
                                          blank=True,
                                          null=True)

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    def clean(self):
        if self.is_transaction != bool(self.related_income):
            raise ValidationError(
                _('If field \'is_transaction\' is True then field \'related_income\' \
                must contain a reference to the associated object. And vice versa.'),
                code='invalid')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
