from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('admin_dep_manage/', views.admin_department_manage, name='admin_dep_manage'),
    path('admin_desig_manage/', views.admin_designation_manage, name='admin_desig_manage'),
    path('admin_qualification_manage/', views.admin_qualification_manage, name='admin_qualification_manage'),
    path('admin_class_manage/', views.admin_class_manage, name='admin_class_manage'),
    path('admin_division_manage/', views.admin_division_manage, name='admin_division_manage'), 
    path('admin_employee_category_manage/', views.admin_employee_category_manage, name='admin_employee_category_manage'),   
    path('edit_dept_ajax/', views.edit_dept_ajax, name='edit_dept_ajax'), 
    path('update_dept_ajax/',views.update_dept_ajax, name='update_dept_ajax'),
    path('delete_dept_ajax/', views.delete_dept_ajax, name='delete_dept_ajax'),
    path('edit_desig_ajax/', views.edit_desig_ajax, name='edit_desig_ajax'),
    path('update_desig_ajax/',views.update_desig_ajax, name='update_desig_ajax'),
    path('delete_desig_ajax/', views.delete_desig_ajax, name='delete_desig_ajax'),
    path('edit_qual_ajax/', views.edit_qualif_ajax, name='edit_qual_ajax'),
    path('update_qualif_ajax/',views.update_qualif_ajax, name='update_qualif_ajax'),
    path('delete_qualif_ajax/', views.delete_qualif_ajax, name='delete_qualif_ajax'),
    path('edit_class_ajax/', views.edit_class_ajax, name='edit_class_ajax'),
    path('update_class_ajax/',views.update_class_ajax, name='update_class_ajax'),
    path('delete_class_ajax/', views.delete_class_ajax, name='delete_class_ajax'),
    path('edit_div_ajax/', views.edit_div_ajax, name='edit_div_ajax'),
    path('update_div_ajax/',views.update_div_ajax, name='update_div_ajax'),
    path('delete_div_ajax/', views.delete_div_ajax, name='delete_div_ajax'),
    path('edit_emp_ajax/', views.edit_emp_ajax, name='edit_emp_ajax'),
    path('update_emp_ajax/',views.update_emp_ajax, name='update_emp_ajax'),
    path('delete_emp_ajax/', views.delete_emp_ajax, name='delete_emp_ajax'),
    path('subject/', views.subject, name='subject'),
    path('edit_sub_ajax/', views.edit_sub_ajax, name='edit_sub_ajax'),
    path('update_sub_ajax/',views.update_sub_ajax, name='update_sub_ajax'),
    path('delete_sub_ajax/', views.delete_sub_ajax, name='delete_sub_ajax'),
    # path('view_sub_ajax"/', views.view_sub_ajax, name='view_sub_ajax'),










     
   
]
