from django.contrib import admin
from .models import MachineryBrandNotebook,CategoryList,Products



class MachineryBrandNotebookAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CategoryListAdmin(admin.ModelAdmin):
    list_display = ('title','url')
    prepopulated_fields = {"url" : ("title",)}

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title','description','price','inventoryNumber','brand','category')



admin.site.register(MachineryBrandNotebook,MachineryBrandNotebookAdmin)
admin.site.register(CategoryList,CategoryListAdmin)
admin.site.register(Products,ProductsAdmin)