from datetime import date

from djmoney.models.fields import MoneyField

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Account(models.Model):

    user = models.ForeignKey(get_user_model(),
                             verbose_name=_('User'),
                             on_delete=models.CASCADE,
                             related_name='accounts',
                             blank=False,
                             null=False)
    name = models.CharField(verbose_name=_('Name'),
                            max_length=50,
                            blank=False,
                            null=False)
    icon = models.CharField(verbose_name=_('Icon of account'),
                            max_length=20,
                            blank=False,
                            null=False)
    initial_balance = MoneyField(verbose_name=_('Initial balance'),
                                 max_digits=10,
                                 decimal_places=2,
                                 blank=False,
                                 null=False)
    balance = MoneyField(verbose_name=_('Total balance'),
                         max_digits=10,
                         decimal_places=2,
                         default=0.00,
                         default_currency='EUR',
                         blank=False,
                         null=False)
    created = models.DateField(verbose_name=_('Date of initial balance'),
                               default=date.today,
                               blank=False,
                               null=False)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
        ordering = ('-name',)

    def __str__(self) -> str:
        return f'{self.name} ({self.user})'

    # def clean(self):
    #     if self.balance_currency != self.initial_balance_currency:
    #         raise ValidationError(_('Currencies of balance and initial_balance must be the same.'))

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)

    @property
    def currency(self) -> str:
        """
        Return currency of the account
        """
        return str(self.balance.currency)

    @property
    def formatted_balance(self) -> str:
        """
        Return formatted balance of the account
        """
        return str(self.balance)
