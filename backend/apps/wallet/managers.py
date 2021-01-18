from typing import Optional

from djmoney.models.managers import understands_money

from django.db.models import Manager, QuerySet
from django.core.exceptions import ObjectDoesNotExist


class WalletQuerySet(QuerySet):

    def by_user_id(self, user_id: int) -> QuerySet:
        return self.filter(user=user_id)

    def by_currency_name(self, currency_name: str) -> QuerySet:
        return self.filter(initial_balance_currency=currency_name)


class WalletManager(Manager):
    """
    Wallet model manager for filtering on various grounds.
    """

    def get_queryset(self):
        return OrderQuerySet(
            model=self.model,
            using=self._db,
        )

    def find(self, wallet_uid: str) -> Optional['Wallet']:
        queryset = self.get_queryset()

        try:
            instance = queryset.get(uid=wallet_uid)
        except ObjectDoesNotExist:
            instance = None
        finally:
            return instance

    def find_by(self, user_id=None, currency_name=None) -> QuerySet:

        if user_id is not None:
            queryset = self.by_user(user_id)

        if currency_name is not None:
            queryset = self.by_currency(currency_name)
