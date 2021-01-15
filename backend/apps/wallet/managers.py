from typing import Optional

from djmoney.models.managers import understands_money

from django.db.models import Manager, QuerySet
from django.core.exceptions import ObjectDoesNotExist


class WalletManager(Manager):
    """
    Wallet model manager for filtering on various grounds.
    """

    def find(self, wallet_uid: str) -> Optional['Wallet']:
        queryset = self.get_queryset()

        try:
            instance = queryset.get(uid=wallet_uid)
        except ObjectDoesNotExist:
            instance = None
        finally:
            return instance

    def find_all_for_user(self, user_id: int) -> QuerySet:
        queryset = self.get_queryset()

        return queryset.filter(user=user_id)

    def find_all_with_currency(self, currency_name: str) -> QuerySet:
        queryset = self.get_queryset()

        return queryset.filter(initial_balance_currency=currency_name)
