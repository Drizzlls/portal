# Generated by Django 4.0.4 on 2022-05-05 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyemployees',
            options={'verbose_name': 'Список сотрудников компании', 'verbose_name_plural': 'Список сотрудников компании'},
        ),
    ]