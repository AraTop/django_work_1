from django.db import models

NULLABLE = {'null':True, 'blank':True}

class Product(models.Model):
   name = models.CharField(max_length=100, verbose_name='Название')
   description = models.TextField(verbose_name='Описание')
   preview = models.ImageField(upload_to='products/', **NULLABLE)
   category = models.CharField(max_length=100, verbose_name='Категория')
   purchase_price = models.IntegerField(verbose_name='Цена за покупку')
   date_of_creation = models.TimeField(verbose_name='дата создания',**NULLABLE)
   last_modified_date = models.TimeField(verbose_name='дата последнего изменения',**NULLABLE)

   def __str__(self):
      return f'{self.name} {self.description} {self.category} {self.purchase_price} {self.date_of_creation} {self.last_modified_date}' 
   
   class Meta:
      verbose_name = 'Продукт'
      verbose_name_plural = 'Продукты'
      ordering = ('name',)

class Category(models.Model):
   name = models.CharField(max_length=100, verbose_name='Название')
   description = models.TextField(verbose_name='Описание')
   created_at = models.TimeField(verbose_name='дата создания', **NULLABLE)

   def __str__(self):
      return f'{self.name} {self.description}' 

   class Meta:
      verbose_name = 'Категория'
      verbose_name_plural = 'Категории'
      ordering = ('name',)