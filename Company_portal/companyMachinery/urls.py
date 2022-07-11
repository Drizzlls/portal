from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MachineryCorp.indexPage,name="IndexMachinery"),
    path('category/<slug:title_category>', MachineryCorp.categoryPage,name="CategoryMachinery"),
    path('add/', MachineryCorp.addPage,name="AddMachinery"),
    path('item/<int:idItem>', MachineryCorp.itemPage,name="itemPage"),
]
