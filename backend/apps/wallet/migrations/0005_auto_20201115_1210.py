# Generated by Django 3.1.3 on 2020-11-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20201113_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]