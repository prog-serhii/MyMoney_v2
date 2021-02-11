import os

from pathlib import Path
from datetime import timedelta
from celery.schedules import crontab


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'm8%o)3$n^03w)mxgvnrxb46__@6qnte9l0dkb7$6%lpbcox+v!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 1)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'djoser',
    'djmoney',
    'djmoney.contrib.exchange',
    'corsheaders',

    'apps.user.apps.UserConfig',
    'apps.wallet.apps.WalletConfig',
    'apps.action.apps.ActionConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('SQL_DATABASE', 'mymoney'),
        'USER': os.environ.get('SQL_USER', 'postgres'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'prog-serhii'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ------------------------------------------ #
#                django-money                #
# ------------------------------------------ #
DEFAULT_CURRENCY = 'EUR'

EXCHANGE_BACKEND = 'djmoney.contrib.exchange.backends.FixerBackend'
FIXER_ACCESS_KEY = 'f5a898dbf45d15d8aa6eca7af3f372e1'

# ------------------------------------------ #
#                  Celery                    #
# ------------------------------------------ #
CELERY_BROKER_URL = os.environ.get('REDIS_LOCATION', 'redis://127.0.0.1:6379')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_LOCATION', 'redis://127.0.0.1:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


CELERY_BEAT_SCHEDULE = {
    'update_rates': {
        'task': 'apps.user.tasks.update_rates',
        'schedule': crontab(hour="*/1"),
    }
}

# ------------------------------------------ #
#           Django REST Framework            #
# ------------------------------------------ #
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

# ------------------------------------------ #
#                   djoser                   #
# ------------------------------------------ #
DJOSER = {
    # Name of a field in User model to be used as login field
    'LOGIN_FIELD': 'email',
    # If True user will be required to click activation
    # link sent in email after:
    # * creating an account
    # * updating their email
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': '/activate/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'eamil/reset/confirm/{uid}/{token}',
    # If True, you need to pass re_password to /users/
    # endpoint, to validate password equality.
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    # If True, register or activation endpoint
    # will send confirmation email to user.
    'SEND_CONFIRMATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'apps.user.serializers.UserCreateSerializer'
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': True,
    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'id',
}

CORS_ALLOW_ALL_ORIGINS = True
