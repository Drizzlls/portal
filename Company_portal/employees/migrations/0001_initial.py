# Generated by Django 4.0.4 on 2022-05-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyEmployees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, null=True, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, null=True, verbose_name='Отчество')),
                ('idАFromBitrix', models.CharField(max_length=9, null=True, verbose_name='Id из Битрикс24')),
            ],
            options={
                'verbose_name': 'Список сотрудников компании',
                'verbose_name_plural': 'Список сотрудников компани',
            },
        ),
    ]
