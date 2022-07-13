from django.urls import path, include
from .views import *

urlpatterns = [
    path('', indexParse,name="IndexEfficiency"),
]
