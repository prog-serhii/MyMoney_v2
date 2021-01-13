from django.db import models


class ExpensesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(expense__isnull=True)


class IncomesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(income__isnull=True)
