from typing import Any, Optional
from django.core.management import BaseCommand

from users.models import User

class Command(BaseCommand):
    
   def handle(self, *args, **options):
      user = User.objects.create(
        email='lololohka057@gmail.com'
         )
      user.set_password('12345')
      user.save()