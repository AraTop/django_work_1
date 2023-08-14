from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
   path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('register/', views.RegisterView.as_view(), name='register'),
   path('profile/', views.ProfileView.as_view(), name='profile'),
   path('profile/genpassword/', views.generate_new_password, name='generate_new_password'),
   path('verify/<slug:token>/', views.verify_email, name='verify_email')
]   