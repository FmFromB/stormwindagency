# Generated by Django 3.1.4 on 2021-02-02 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stormwind_app', '0006_auto_20210202_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stormwind_app.client', verbose_name='Клиент'),
        ),
    ]
