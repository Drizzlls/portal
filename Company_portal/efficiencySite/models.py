from django.db import models

# Create your models here.

class EfficiencySiteControl(models.Model):
    link = models.URLField(max_length=250, null=True, verbose_name="Ссылка на сайт")
    title = models.CharField(max_length=250,null=True,verbose_name="Название сайта")
    statusNow = models.CharField(max_length=3,null=True,verbose_name="Статус сейчас")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список сайтов"
        verbose_name_plural = "Список сайтов"

class EfficiencySiteStatus(models.Model):
    date = models.DateTimeField(auto_now_add=True,verbose_name="Дата")
    status = models.CharField(max_length=3,null=True,verbose_name="Статус")
    site = models.ForeignKey(EfficiencySiteControl,on_delete=models.CASCADE, verbose_name="Сайт",null=True)

