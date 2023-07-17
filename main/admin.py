from django.contrib import admin
from main.models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'description','category','purchase_price','date_of_creation','last_modified_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'description')