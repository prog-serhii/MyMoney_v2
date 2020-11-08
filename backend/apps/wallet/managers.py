from django.db.models import Manager, QuerySet


class WalletQuerySet(QuerySet):
    def by_user(self, user):
        """
        Filtering by user id.
        """
        return self.filter(user=user)

    def by_currency(self, currency):
        """
        Filtering by currency code.
        """
        return self.filter(start_balance_currency=currency)

    def active(self):
        """
        Filtering by active items.
        """
        return self.filter(active=True)


class WalletManager(Manager):
    """
    Wallet model manager for filtering on various grounds.
    """

    def get_queryset(self):
        """
        Get custom Wallet query set.
        """
        return WalletQuerySet(self.model, using=self._db)

    def by_user(self, user):
        return self.get_queryset().by_user(user)

    def by_currency(self, currency):
        return self.get_queryset().by_currency(currency)

    def active(self):
        return self.get_queryset().active()
