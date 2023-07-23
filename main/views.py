from django.shortcuts import get_object_or_404, render

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

def product_detail(request, pk):
   product_ = get_object_or_404(Product, pk=pk)
   context = {
        'object': product_
   }
   return render(request, "main/product_detail.html", context)