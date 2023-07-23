from django import template
from django.conf import settings
import os

register = template.Library()

@register.simple_tag
def mediapath(image_path):
   media_url = settings.MEDIA_URL
   full_path = os.path.join(media_url, image_path)
   return full_path