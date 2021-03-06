# Generated by Django 3.1.4 on 2021-02-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stormwind_app', '0012_auto_20210206_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=100, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.PositiveIntegerField(verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='property',
            name='floor',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='property',
            name='floor_count',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество этажей'),
        ),
        migrations.AlterField(
            model_name='property',
            name='number_flat',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='property',
            name='number_home',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='property',
            name='rooms',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='commission',
            field=models.PositiveIntegerField(null=True, verbose_name='Комиссия'),
        ),
        migrations.AlterField(
            model_name='req',
            name='max_area',
            field=models.PositiveIntegerField(null=True, verbose_name='Максимальная площадь (кв. метров)'),
        ),
        migrations.AlterField(
            model_name='req',
            name='max_floor',
            field=models.PositiveIntegerField(null=True, verbose_name='До'),
        ),
        migrations.AlterField(
            model_name='req',
            name='max_floor_count',
            field=models.PositiveIntegerField(null=True, verbose_name='До'),
        ),
        migrations.AlterField(
            model_name='req',
            name='max_price',
            field=models.PositiveIntegerField(null=True, verbose_name='До'),
        ),
        migrations.AlterField(
            model_name='req',
            name='max_room_count',
            field=models.PositiveIntegerField(null=True, verbose_name='Максимальное количество комнат'),
        ),
        migrations.AlterField(
            model_name='req',
            name='min_area',
            field=models.PositiveIntegerField(null=True, verbose_name='Минимальная площадь (кв. метров)'),
        ),
        migrations.AlterField(
            model_name='req',
            name='min_floor',
            field=models.PositiveIntegerField(null=True, verbose_name='Этаж от'),
        ),
        migrations.AlterField(
            model_name='req',
            name='min_floor_count',
            field=models.PositiveIntegerField(null=True, verbose_name='Количество этажей от'),
        ),
        migrations.AlterField(
            model_name='req',
            name='min_price',
            field=models.PositiveIntegerField(null=True, verbose_name='Цена от'),
        ),
        migrations.AlterField(
            model_name='req',
            name='min_room_count',
            field=models.PositiveIntegerField(null=True, verbose_name='Минимальное количество комнат'),
        ),
    ]
