from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import EfficiencySiteControl


class ControlSite:
    def IndexEfficiency(request):
        url = EfficiencySiteControl.objects.get(pk=1)
        print(ControlSite.parseSite(site=url.link))
        return HttpResponse("Все ок")

    def parseSite(site):
        page = requests.get(site)
        return page.status_code

