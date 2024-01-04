from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
  
]
