from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'register_login'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/Login.html')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'), name='password_reset'),
]