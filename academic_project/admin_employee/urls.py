from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('admin_emp_add/', views.admin_emp_add, name='admin_emp_add'),
    path('admin_emp_view/', views.admin_emp_view, name='admin_emp_view'),
    path('get_subjects_for_class/', views.get_subjects_for_class, name='get_subjects_for_class'),
    path('emp_list/', views.emp_list, name='emp_list'),
    path('admin_emp_edit/<int:itm_id>/', views.admin_emp_edit, name='admin_emp_edit'),
   
   
]