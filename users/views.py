import random
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from config import settings
from users.forms import UserForm, UserProfileForm
from users.models import User
from django.core.mail import send_mail

class RegisterView(CreateView):
   model = User
   form_class = UserForm
   template_name = 'users/users_register.html'
   success_url = '/users/login/'
   

class ProfileView(UpdateView):
   model = User
   form_class = UserProfileForm
   success_url = reverse_lazy("users:profile")

   def get_object(self, queryset=None):
      return self.request.user
      
def generate_new_password(request):
   new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
   send_mail(
      subject='Вы сменили пароль',
      message=f'Ваш новый пароль: {new_password}',
      from_email=settings.EMAIL_HOST_USER,
      recipient_list=[request.user.email]
   )
   request.user.set_password(new_password)
   request.user.save()
   return redirect(reverse('users:profile'))