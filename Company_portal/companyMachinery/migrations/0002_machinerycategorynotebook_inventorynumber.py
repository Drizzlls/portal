# Generated by Django 4.0.4 on 2022-06-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyMachinery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinerycategorynotebook',
            name='inventoryNumber',
            field=models.CharField(max_length=11, null=True, verbose_name='Инвентаризационный номер'),
        ),
    ]
