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
   number_of_views = models.IntegerField(verbose_name='Просмотры', **NULLABLE, default=0)

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

class Blog(models.Model):
   header = models.CharField(max_length=100, verbose_name='заголовок')
   slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
   content = models.CharField(max_length=250, verbose_name='Cодержимое')
   preview = models.ImageField(upload_to='blogs/', **NULLABLE, verbose_name='превью ')
   date_creation = models.TimeField(verbose_name='Дата создания', **NULLABLE)
   is_publication = models.BooleanField(verbose_name='Опубликовано')
   number_of_views = models.IntegerField(verbose_name='Просмотры', **NULLABLE, default=0)

   def __str__(self):
      return f'{self.header} {self.slug} {self.content} {self.date_creation} {self.is_publication} {self.number_of_views}' 
   
   class Meta:
      verbose_name = 'Статья'
      verbose_name_plural = 'Статьи'
      ordering = ('header',)

class Version(models.Model):
   version_number =  models.IntegerField(verbose_name='Номер версии')
   version_name =  models.CharField(max_length=100, verbose_name='Название версии')
   is_active_version = models.BooleanField(verbose_name='Признак версии')
   product = models.ForeignKey(Product, related_name='version', on_delete=models.CASCADE)
   
   def __str__(self):
      return f'{self.version_number} {self.version_name} {self.is_active_version} {self.product}' 
   
   class Meta:
      verbose_name = 'Версия'
      verbose_name_plural = 'Версии'
      ordering = ('version_number',)