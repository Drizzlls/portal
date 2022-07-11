from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ControlSite.IndexEfficiency,name="IndexEfficiency"),
]
