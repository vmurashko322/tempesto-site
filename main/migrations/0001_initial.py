# Generated by Django 3.2.5 on 2021-08-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=150, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=150, verbose_name='Телефон')),
                ('equipment', models.CharField(max_length=200, verbose_name='Какое оборудование Вам нужно?')),
                ('load', models.CharField(max_length=200, verbose_name='Мощность и тип нагрузки?')),
                ('time_working', models.CharField(max_length=150, verbose_name='Время автономной работы?')),
            ],
        ),
    ]
