from django.shortcuts import render

from main.models import Product


def index(request):
   products_list = Product.objects.all()
   context = {
      'object_list':products_list
   }
   return render(request, "main/index.html", context)

def products(request):
   products_list = Product.objects.all()
   context = {
      'object_list':products_list
   }
   return render(request, "main/products.html", context) 