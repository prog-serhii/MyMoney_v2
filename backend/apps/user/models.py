from djmoney.models.fields import CurrencyField

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # default value is setup in DEFAULT_CURRENCY (settings.py)
    main_currency = CurrencyField(verbose_name='Main currency')

    objects = UserManager()

    USERNAME_FIELD = 'email'
