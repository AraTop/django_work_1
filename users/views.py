import random
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from config import settings
from users.forms import UserForm, UserProfileForm
from users.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

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
            message=f'Пожалуйста, нажмите на следующую ссылку, чтобы подтвердить свой адрес электронной почты: {confirmation_url}',
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

def verify_email(request, token):
   try:
      user_id = force_str(urlsafe_base64_decode(token))
      user = User.objects.get(pk=user_id, is_active=True)
      if default_token_generator.check_token(user, token):
         user.is_email_verified = True
         user.email_confirmation_token = None
         user.save()
         return render(request, 'users/email_verified.html', {'verified': True})
      else:
         return render(request, 'users/email_verified.html', {'verified': False})
   except (TypeError, ValueError, OverflowError, User.DoesNotExist):
      return render(request, 'users/email_verification_error.html')