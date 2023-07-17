from typing import Any, Optional
from django.core.management import BaseCommand

from main.models import Product , Category

class Command(BaseCommand):
    
   def handle(self, *args, **options):
      Category.objects.all().delete()
      Product.objects.all().delete()

      product_list = [
         {'name':'Сабака', 'description':'Гавкает', 'category':'Злая', 'purchase_price':10000, 'date_of_creation':None, 'last_modified_date':None},
         {'name':'Кошка', 'description':'Бегает', 'category':'Злая', 'purchase_price':6000, 'date_of_creation':None, 'last_modified_date':None},
         {'name':'Зайчик', 'description':'Прыгает', 'category':'Милый', 'purchase_price':1000, 'date_of_creation':None, 'last_modified_date':None},
         {'name':'Скунс', 'description':'Пукает', 'category':'не туда ни сюда', 'purchase_price':5000, 'date_of_creation':None, 'last_modified_date':None},
         {'name':'Таракан', 'description':'Кусается', 'category':'Страшный', 'purchase_price':100, 'date_of_creation':None, 'last_modified_date':None}
      ]
      product_list_create = []
      for product_item in product_list:
         product_list_create.append(
            Product(**product_item)
         )
      Product.objects.bulk_create(product_list_create) 

      category_list = [
         {'name':'Сабака', 'description':'Гавкает', 'created_at':None},
         {'name':'Кошка', 'description':'Бегает', 'created_at':None},
         {'name':'Зайчик', 'description':'Прыгает', 'created_at':None},
         {'name':'Скунс', 'description':'Пукает', 'created_at':None},
         {'name':'Таракан', 'description':'Кусается', 'created_at':None}
      ]
      category_list_create = []
      for category_item in category_list:
         category_list_create.append(
            Category(**category_item)
         )
      Category.objects.bulk_create(category_list_create) 

