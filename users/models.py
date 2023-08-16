from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null':True, 'blank':True}

class User(AbstractUser):
   username = None
   email = models.EmailField(unique=True, verbose_name='Почта')

   phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
   avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)
   contry = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)

   email_confirmation_token = models.CharField(max_length=255, **NULLABLE)
   is_email_verified = models.BooleanField(default=False)

   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = []
