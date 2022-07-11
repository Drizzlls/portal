from django.db import models

# Create your models here.

class EfficiencySiteControl(models.Model):
    link = models.URLField(max_length=250, null=True, verbose_name="Ссылка на сайт")
    title = models.CharField(max_length=250,null=True,verbose_name="Название сайта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список сайтов"
        verbose_name_plural = "Список сайтов"
