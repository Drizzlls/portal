from django.db import models

# Create your models here.

class CompanyEmployees(models.Model):
    name = models.CharField(max_length=50,null=True,verbose_name="Имя")
    surname = models.CharField(max_length=50, null=True, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, null=True, verbose_name="Отчество")
    idАFromBitrix = models.CharField(max_length=9, null=True, verbose_name="Id из Битрикс24")
    position = models.CharField(max_length=50, null=True, verbose_name="Должность")
    isActive = models.CharField(max_length=5,verbose_name="Активен или нет")

    class Meta:
        verbose_name = "Список сотрудников компании"
        verbose_name_plural = "Список сотрудников компании"
