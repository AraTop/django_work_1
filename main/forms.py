from django import forms
from main.models import Product, Version

class ProductForm(forms.ModelForm):
    
   class Meta:
      model = Product 
      fields = '__all__'
 
   def clean(self):
      cleaned_data = super().clean()
      name = cleaned_data.get('name')
      forbidden_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'] 

      description = cleaned_data.get('description')
      forbidden_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

      if name.lower() in forbidden_products:
         self.add_error('name', "Вы не можете в поле 'Название' создавать товары с запрещенным названием.")
        
      if description.lower() in forbidden_products:
         self.add_error('description', "Вы не можете в поле 'Описание' создавать товары с запрещенным описанием.")


class VersionForm(forms.ModelForm):

   class Meta:
      model = Version
      fields = '__all__'