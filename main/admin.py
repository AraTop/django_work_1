from django.contrib import admin
from main.models import Blog, Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'description','category','purchase_price','date_of_creation','last_modified_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'description')

@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('header', 'slug', 'content', 'date_creation', 'is_publication', 'number_of_views')