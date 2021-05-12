from django.urls import path
from .views import *

app_name = 'register_login'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
]