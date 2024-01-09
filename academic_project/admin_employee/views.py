from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse,HttpResponse
from admin_master.models import Academicdesignation,Academicqualification,Academicdepartment,Academicemployee

# Create your views here.
def admin_emp_add(request):
    emp=Academicdesignation.objects.filter(desigstatus=1)
    qualif=Academicqualification.objects.filter(qualificationstatus=1)
    dept=Academicdepartment.objects.filter(deptstatus=1)
    ademp=Academicemployee.objects.filter(employee_cat_status=1)

    return render(request,'admin_emp_add.html',{'emp':emp,'qualif':qualif,'dept':dept,'ademp':ademp})