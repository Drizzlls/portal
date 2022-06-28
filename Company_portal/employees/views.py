import pprint
from django.shortcuts import render
from django.http import HttpResponse
from bitrix24 import *
from .models import CompanyEmployees

class UsersFromBitrix:
    def generateUsers():
        webhook = "https://novoedelo.bitrix24.ru/rest/16/3lhovi0rx5bcsqif/"
        b = Bitrix24(webhook)
        getUsers = b.callMethod( "user.get")
        for user in getUsers:
            # pprint.pprint(sotrudn)
            try:
                sot = CompanyEmployees.objects.get(idАFromBitrix=user['ID'])
            except:
                form = CompanyEmployees(
                    name=f"{user['NAME']}",
                    surname=f"{user['LAST_NAME']}",
                    idАFromBitrix=f"{user['ID']}",
                    position=f"{user['WORK_POSITION']}",
                    isActive = f"{user['ACTIVE']}"
                )
                form.save()

    def loadUsers(request):
        UsersFromBitrix.generateUsers()

    def showListUsers(request):
        users = CompanyEmployees.objects.all()
        return render(request,"employees/index.html",{"users":users})

    def profile(request,idSotr):
        sotr = CompanyEmployees.objects.get(idАFromBitrix=idSotr)
        return render(request,"employees/profile.html",{"sotr":sotr})