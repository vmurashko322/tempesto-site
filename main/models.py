from django.db import models


class Request(models.Model):
    name_surname = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=150, verbose_name='Телефон')
    equipment = models.CharField(max_length=200, verbose_name='Какое оборудование Вам нужно?')
    load = models.CharField(max_length=200, verbose_name='Мощность и тип нагрузки?')
    time_working = models.CharField(max_length=150, verbose_name='Время автономной работы?')