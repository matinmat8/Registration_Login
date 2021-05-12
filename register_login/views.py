from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'register_login/index.html')