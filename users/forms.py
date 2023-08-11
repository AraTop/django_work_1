from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from main.forms import StyleFormMixin

class UserForm(UserCreationForm):
   
   class Meta:
      model = User
      fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):

   class Meta:
      model = User
      fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'contry')