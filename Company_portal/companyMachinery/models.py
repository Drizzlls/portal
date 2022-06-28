from django.db import models
# Create your models here.



class MachineryBrandNotebook(models.Model):
    name = models.CharField(max_length=15, null=True, verbose_name="Название бренда")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Список брендов ноутбуков"
        verbose_name_plural = "Список брендов ноутбуков"


class CategoryList(models.Model):
    title = models.CharField(max_length=50,verbose_name="Название категории")
    url = models.SlugField(max_length = 50,verbose_name="Slug",unique=True,db_index=True)

    class Meta:
        verbose_name = "Cписок категорий"
        verbose_name_plural = "Список категорий"

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=75, null=True, verbose_name="Название")
    description = models.CharField(max_length=355, null=True, verbose_name="Описание")
    price = models.CharField(max_length=11, null=True, verbose_name="Цена покупки")
    inventoryNumber = models.CharField(max_length=11, null=True, verbose_name="Инвентаризационный номер")
    brand = models.ForeignKey(MachineryBrandNotebook, on_delete=models.CASCADE,verbose_name="Бред")
    category = models.ForeignKey(CategoryList, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Технику"
        verbose_name_plural = "Техника"