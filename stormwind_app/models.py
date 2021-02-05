from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    PROPERTY_TYPES = [
        ('Дом','Дом'),
        ('Квартира', 'Квартира'),
        ('Земля', 'Земля')
        ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', null=True, blank=True)
    city = models.CharField('Город', max_length=15, null=True, blank=True)
    street = models.CharField('Улица', max_length=15, null=True, blank=True)
    number_home = models.IntegerField('Дом', null=True, blank=True)
    number_flat = models.IntegerField('Квартира', null=True, blank=True)
    floor = models.IntegerField('Этаж', null=True, blank=True)
    rooms = models.IntegerField('Количество комнат', null=True, blank=True)
    area = models.IntegerField('Площадь')
    floor_count = models.IntegerField('Количество этажей', null=True, blank=True)
    property_type = models.CharField('Тип собственности', choices=PROPERTY_TYPES, max_length=20, null=True)

    class Meta:
        verbose_name='запрос'
        verbose_name_plural='запросы'

    def __str__(self):
        return str(self.id)

class Client(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', null=True, blank=True)
    first_name = models.CharField('Имя', max_length=100, null=True)
    last_name = models.CharField('Фамилия', max_length=100, null=True)
    middle_name = models.CharField('Отчество', max_length=100, null=True)
    phone = models.CharField('Телефон', max_length=100, null=True)
    email = models.CharField('Email', max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class Realtor(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', null=True, blank=True)
    first_name = models.CharField('Имя', max_length=100, null=True)
    last_name = models.CharField('Фамилия', max_length=100, null=True)
    middle_name = models.CharField('Отчество', max_length=100, null=True)
    commission = models.IntegerField('Комиссия', null=True)

    def __str__(self):
        return str(self.id)

class Offer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор обьявления', null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Номер клиента', null=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE, verbose_name='Номер риэлтора', null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='Номер недвижимости', null=True)
    price = models.IntegerField('Цена', null=True)
    price_percent = models.IntegerField('Цена c процентами', blank=True, null=True)

    class Meta:
        verbose_name='предложение'
        verbose_name_plural='Предложения'

    def __str__(self):
        return str(self.id)

class Req(models.Model):
    PROPERTY_TYPES = [
        ('Дом','Дом'),
        ('Квартира', 'Квартира'),
        ('Земля', 'Земля')
        ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор обьявления', null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Номер клиента', null=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE, verbose_name='Номер риэлтора', null=True)
    property_type = models.CharField('Тип имущества', choices=PROPERTY_TYPES, max_length=100)
    min_price = models.IntegerField('Цена от', null=True)
    max_price = models.IntegerField('До', null=True)
    min_area = models.IntegerField('Минимальная площадь (кв. метров)', null=True)
    max_area = models.IntegerField('Максимальная площадь (кв. метров)', null=True)
    min_room_count = models.IntegerField('Минимальное количество комнат', null=True)
    max_room_count = models.IntegerField('Максимальное количество комнат', null=True)
    min_floor = models.IntegerField('Этаж от', null=True)
    max_floor = models.IntegerField('До', null=True)
    min_floor_count = models.IntegerField('Количество этажей от', null=True)
    max_floor_count = models.IntegerField('До', null=True)

    def __str__(self):
        return str(self.id)

class Deal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор сделки', null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, verbose_name='Номер предложения', null=True)
    req = models.ForeignKey(Req, on_delete=models.CASCADE, verbose_name='Номер запроса', null=True)




