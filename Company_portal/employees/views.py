import pprint
from django.shortcuts import render
from django.http import HttpResponse
from bitrix24 import *
from .models import CompanyEmployees



# Создать класс с методами битрикса(гет,адд и т.д)
class UsersFromBitrix:
    def generateUsers():
        webhook = "https://novoedelo.bitrix24.ru/rest/16/rze2rg3z1cdu9ua7/"
        b = Bitrix24(webhook)
        getUsers = b.callMethod("user.get")
        for user in getUsers:
            try:
                updateData = CompanyEmployees.objects.get(idАFromBitrix=user['ID'])
                form = updateData(name=f"{user['NAME']}",
                    surname=f"{user['LAST_NAME']}",
                    idАFromBitrix=f"{user['ID']}",
                    position=f"{user['WORK_POSITION']}",
                    isActive = f"{user['ACTIVE']}")
                form.save()
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
        try:
            return HttpResponse('Загрузка прошла успешно')

        except:
            return HttpResponse('Что то пошло не так')

    def showListUsers(request):
        users = CompanyEmployees.objects.all()
        return render(request,"employees/index.html",{"users":users})

    def profile(request,idSotr):
        sotr = CompanyEmployees.objects.get(idАFromBitrix=idSotr)
        return render(request,"employees/profile.html",{"sotr":sotr})


def addPerson(request):
    webhook = "https://novoedelo.bitrix24.ru/rest/16/rze2rg3z1cdu9ua7/"
    b = Bitrix24(webhook)
    try:
        addUser = b.callMethod('user.add',EMAIL=request.POST["EMAIL"],UF_DEPARTMENT=1,LAST_NAME=request.POST["LAST_NAME"],NAME=request.POST["NAME"] )
        return HttpResponse("Все ок тут")
    except BitrixError as message:
        return HttpResponse(message)

def registrationUser(request):
    return render(request, "employees/registration.html")
