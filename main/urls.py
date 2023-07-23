from django.urls import path
from main import views

urlpatterns = [
   path("", views.index),
   path("products/", views.products),
   path('product/<int:pk>/', views.product_detail),
]  