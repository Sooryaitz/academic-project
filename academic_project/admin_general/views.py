from django.shortcuts import redirect, render
from django.template  import loader

# Create your views here.

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

