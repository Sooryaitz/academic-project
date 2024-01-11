from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('admin_emp_add/', views.admin_emp_add, name='admin_emp_add'),
    path('get_subjects_for_class/', views.get_subjects_for_class, name='get_subjects_for_class'),
   
]