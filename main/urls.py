from django.urls import path
from main.views import index , products

urlpatterns = [
   path("", index),
   path("contacts/", products)
]