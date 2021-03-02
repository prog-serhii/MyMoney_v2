from djmoney.models.fields import CurrencyField

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    main_currency = CurrencyField(verbose_name=_('Main currency'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    def save(self, *args, **kwargs):
        created = self._state.adding
        super(User, self).save(*args, **kwargs)

        if created:
            from .services import (create_initial_income_categories,
                                   create_initial_expense_categories)
            create_initial_income_categories(self)
            create_initial_expense_categories(self)
