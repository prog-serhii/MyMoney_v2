from datetime import date
from djmoney.models.managers import understands_money

from django.db.models import Manager, QuerySet


class ExpenseQuerySet(QuerySet):
    @understands_money
    def user(self, user):
        return self.filter(user=user)

    @understands_money
    def date_range(self, start_date, end_date):
        return self.filter(date__range=(start_date, end_date))

    @understands_money
    def date(self, year=None, month=None, day=None):
        """
        Filtering objects by date range (year, month or day)

        date() - return all objects created today
        date(year=2019) - return all objects created in 2019 year
        date(year=2020, month=1) - return all objects created in the 1-th month of 2020.
        date(year=2020, month=1, day=1) - return all objects created
                                        on 1-th day of 1-th month and 2020 year.
        date(year=2020, day=1) - return all objects created
                                on 1-th day of current month and 2020 year.
        """
        today = date.today()

        if day:
            # returns objects created on a specific day

            # check if there are a month and a year,
            # if not - then set the current ones
            year = year if year else today.year
            month = month if month else today.month

            return self.filter(date__year=year, date__month=month, date__day=day)

        elif month:
            # returns objects created on a specific month

            # check if there is a year, if not - then set the current year
            year = year if year else today.year

            return self.filter(date__year=year, date__month=month)

        elif year:
            # returns objects created on a specific year

            return self.filter(date__year=year)

        else:
            # returns objects created today

            return self.filter(
                date__year=today.year,
                date__month=today.month,
                date__day=today.day
            )


class ExpenseManager(Manager):
    """
    Expense model manager for filtering on various grounds.
    """

    def get_queryset(self):
        """
        Get custom Wallet query set.
        """
        return ExpenseQuerySet(self.model, using=self._db)

    def user(self, user):
        """
        Filtering by user id.
        """
        return self.get_queryset().user(user)

    def date_range(self, start_date, end_date=date.today()):
        """
        Filtering by date range.
        """
        return self.get_queryset().date_range(start_date, end_date)

    def date(self, year=None, month=None, day=None):
        """
        Filtering by date range (year, month, day).
        """
        return self.get_queryset().date(year, month, day)
