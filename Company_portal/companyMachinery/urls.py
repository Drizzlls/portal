from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MachineryCorp.indexPage),
    path('category/<slug:title_category>', MachineryCorp.categoryPage),
    path('add/', MachineryCorp.addPage,name="Добавление техники"),

]
