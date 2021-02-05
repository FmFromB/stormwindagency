# Generated by Django 3.1.4 on 2021-02-03 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stormwind_app', '0008_auto_20210202_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор сделки'),
        ),
    ]
