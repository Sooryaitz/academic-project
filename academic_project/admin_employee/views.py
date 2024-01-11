from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse,HttpResponse
from admin_master.models import *
from django.views.decorators.http import require_GET

# Create your views here.
def admin_emp_add(request):
    emp=Academicdesignation.objects.filter(desigstatus=1)
    qualif=Academicqualification.objects.filter(qualificationstatus=1)
    dept=Academicdepartment.objects.filter(deptstatus=1)
    ademp=Academicemployee.objects.filter(employee_cat_status=1)
    cls=Academicclass.objects.filter(classstatus=1)
    div=Academicdivision.objects.filter(divisionstatus=1)
    sub=AcademicSubject.objects.filter(subjectstatus=1)
    

    return render(request,'admin_emp_add.html',{'emp':emp,'qualif':qualif,'dept':dept,'ademp':ademp,'cls':cls,'div':div,'sub':sub})

def get_subjects_for_class(request):
    class_id = request.GET.get('class_id')
    
    subjects = SubjectFore.objects.filter(classid_id=class_id).values('subjectid__id', 'subjectid__subjectclass')
    
    return JsonResponse(list(subjects), safe=False)