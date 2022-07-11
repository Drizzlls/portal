from django.contrib import admin
from .models import EfficiencySiteControl


class EfficiencySiteAdmin(admin.ModelAdmin):
    list_display = ('link','title')



admin.site.register(EfficiencySiteControl,EfficiencySiteAdmin)