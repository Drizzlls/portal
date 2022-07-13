from django.urls import path, include
from .views import *

urlpatterns = [
    path('',indexPage,name="IndexMachinery"),
    path('category/<slug:title_category>',categoryPage,name="CategoryMachinery"),
    path('add/',addPage,name="AddMachinery"),
    path('item/<int:idItem>',itemPage,name="itemPage"),
    path('delete/<int:id>',deleteItem,name="DeleteItemPage"),
]
