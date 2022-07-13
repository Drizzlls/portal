from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import EfficiencySiteControl,EfficiencySiteStatus


def loadData():
    sites = EfficiencySiteControl.objects.all()

    for site in sites:
        # Получаем текущую ссылку на сайт
        searchSite = EfficiencySiteControl.objects.get(link=site.link)

        # Записываем текущий статус и связь с таблицей с сайтами в таблицу с ответами
        saveData = EfficiencySiteStatus(status=parseSite(site.link),site=searchSite)

        # Записываем текущий статус в таблицу с сайтами
        searchSite.statusNow = parseSite(site.link)

        # Сохраняем данные
        searchSite.save()
        saveData.save()

def indexParse(request):
    loadData()
    data = EfficiencySiteControl.objects.all()
    return render(request,"effinciencySite/index.html",{"data":data})


def parseSite(site):
    page = requests.get(site)
    return page.status_code

