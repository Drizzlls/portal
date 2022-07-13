from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MachineryBrandNotebook,Products,CategoryList
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.
def indexPage(request):
    listCategory = CategoryList.objects.all()
    return render(request, "machinery/category/listCategory.html", {"listCategory": listCategory})


def categoryPage(request, title_category):
    getcategory = CategoryList.objects.get(url=title_category).id
    listOfProductsInTheCategory = Products.objects.filter(category=getcategory)
    return render(request, "machinery/category/category.html", {"listProducts": listOfProductsInTheCategory})


def addPage(request):
    if request.method == "POST":
        form = AddItem(request.POST)
        form.save()
    else:
        form = AddItem()
    return render(request, "machinery/add.html", {"form": form})


def itemPage(request, idItem):
    item = Products.objects.get(pk=idItem)
    return render(request, "machinery/itemPage.html", {"item": item})


def deleteItem(request,id):
    # itemForDelete = Products.objects.get(pk=id).delete()
    print(request.META.get('HTTP_REFERER'))
    return redirect('IndexMachinery',permanent=True)


