from django.shortcuts import render
from django.http import HttpResponse
from .models import MachineryBrandNotebook,Products,CategoryList
from .forms import *

# Create your views here.
class MachineryCorp:
    def indexPage(request):
        listCategory = CategoryList.objects.all()
        return render(request, "machinery/category/listCategory.html",{"listCategory":listCategory})

    def categoryPage(request,title_category):
        getcategory = CategoryList.objects.get(url=title_category).id
        listOfProductsInTheCategory = Products.objects.filter(category=getcategory)
        return render(request, "machinery/category/category.html",{"listProducts" : listOfProductsInTheCategory})

    def addPage(request):
        if request.method == "POST":
            form = AddItem(request.POST)
            form.save()
        else:
            form = AddItem()
        return render(request, "machinery/add.html",{"form":form})
