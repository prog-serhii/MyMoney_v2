# Generated by Django 3.1.5 on 2021-03-01 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0002_auto_20210226_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transfers', to='authentication.user', verbose_name='User'),
            preserve_default=False,
        ),
    ]
