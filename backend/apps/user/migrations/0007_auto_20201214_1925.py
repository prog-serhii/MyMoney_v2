# Generated by Django 3.1.3 on 2020-12-14 19:25

import django.contrib.postgres.fields
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201214_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currencies',
            field=django.contrib.postgres.fields.ArrayField(base_field=djmoney.models.fields.CurrencyField(blank=True, default='EUR', max_length=3), size=5),
        ),
    ]
