from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TransactionConfig(AppConfig):
    name = 'apps.transaction'
    verbose_name = _('Transaction')
