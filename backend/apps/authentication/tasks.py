from celery import shared_task

from djmoney.contrib.exchange.backends import FixerBackend


@shared_task
def update_rates():
    FixerBackend().update_rates()
    print("Rates are updated!")
