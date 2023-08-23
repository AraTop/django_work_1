import random
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from config import settings
from users.forms import UserForm, UserProfileForm
from users.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login

class RegisterView(CreateView):
   model = User
   form_class = UserForm
   template_name = 'users/users_register.html'
   success_url = '/users/login/'
   
   def form_valid(self, form):
      response = super().form_valid(form)
      token = default_token_generator.make_token(self.object)
      confirmation_url = self.request.build_absolute_uri(reverse_lazy('users:verify_email', args=[token]))
      self.object.email_confirmation_token = token
      self.object.save()
      send_mail(
         subject='Подтвердите ваш адрес электронной почты',
         message=f'Пожалуйста нажмите на следующую ссылку, чтобы подтвердить свой адрес электронной почты: {confirmation_url}',
         from_email=settings.EMAIL_HOST_USER,
         recipient_list=[self.object.email]
      )
      return response
   
@method_decorator(login_required, name='dispatch')  
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

@method_decorator(login_required, name='dispatch')  
class VerifyEmail(TemplateView):
   def get(self, request, *args, **kwargs):
     print(request.user.email_confirmation_token)
     key = request.user.email_confirmation_token
     user = User.objects.filter(email_confirmation_token=key).first()
     if user:
         request.user.is_email_verified = True
         request.user.email_confirmation_token = None
         request.user.save()
         return redirect('/') 
     else:
         return 