from django.contrib import admin
from .models import CompanyEmployees



class CompanyEmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'idАFromBitrix')


admin.site.register(CompanyEmployees,CompanyEmployeesAdmin)