# Generated by Django 4.0.5 on 2022-07-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efficiencySite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='efficiencysitecontrol',
            name='title',
            field=models.CharField(max_length=250, null=True, verbose_name='Название сайта'),
        ),
    ]
