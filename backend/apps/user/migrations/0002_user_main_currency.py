# Generated by Django 3.1.3 on 2020-12-14 18:05

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='main_currency',
            field=djmoney.models.fields.CurrencyField(default='XYZ', max_length=3, verbose_name='Main currency'),
        ),
    ]
