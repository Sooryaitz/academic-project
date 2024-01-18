from django.shortcuts import render
from admin_master.models import Academicclass,Academicqualification,Academicdivision,Academicdepartment,Academicdesignation,AcademicSubject,Academicemployee,SubjectFore
from .models import adminemp,empdesig,empdpt,salary,scd
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
import qrcode
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.

def admin_emp_add(request):
    emp=Academicdesignation.objects.filter(desigstatus=1)
    qualif=Academicqualification.objects.filter(qualificationstatus=1)
    dept=Academicdepartment.objects.filter(deptstatus=1)
    ademp=Academicemployee.objects.filter(employee_cat_status=1)
    cls=Academicclass.objects.filter(classstatus=1)
    div=Academicdivision.objects.filter(divisionstatus=1)
    sub=AcademicSubject.objects.filter(subjectstatus=1)
    
    context={
        'qualification_data':qualif,
        'designation_data':emp,
        'department_data':dept,
        'employee_data':ademp,
        'class_data':cls,
        'division_data':div,
        'subject_data':sub,

    }
    
    return render(request,'admin_emp_add.html',context)             
    
def admin_emp_view(request):
    emp=Academicdesignation.objects.filter(desigstatus=1)
    qualif=Academicqualification.objects.filter(qualificationstatus=1)
    dept=Academicdepartment.objects.filter(deptstatus=1)
    ademp=Academicemployee.objects.filter(employee_cat_status=1)
    cls=Academicclass.objects.filter(classstatus=1)
    div=Academicdivision.objects.filter(divisionstatus=1)
    sub=AcademicSubject.objects.filter(subjectstatus=1)

    
    if request.method == 'POST':
       
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        department = request.POST.get('department')
        jdate = request.POST.get('joindate')

        qr_data = f"Name: {fname} {lname}\nDOB: {dob}\nDepartment: {department}\nJoin Date: {jdate}"

        # Generate QR code image
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to a BytesIO object
        qr_image_io = BytesIO()
        img.save(qr_image_io, format='PNG')
        qr_image_io.seek(0)

        # Create an InMemoryUploadedFile from BytesIO
        qr_image = InMemoryUploadedFile(
            file=qr_image_io,
            field_name=None,
            name=f'qr_code_{fname}_{lname}.png',
            content_type='image/png',
            size=qr_image_io.tell(),
            charset=None,
        )



        employee = adminemp.objects.create(
            empcatid_id=json.loads(request.POST.get('emp_cat_id')).get('id'),
            empname=fname + ' ' + lname,
            dob=request.POST.get('dob'),
            mobile=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            joindate=request.POST.get('joindate'),
            photo=request.FILES.get('photo'),
            qualifid_id=request.POST.get('qualification'),
            desigid_id=request.POST.get('designation'),
            dptid_id=request.POST.get('department'),
            salary=request.POST.get('salary'),
            gender=request.POST.get('gender'),
            barcode=qr_image,
        )

        # Handle empdesig
        empdesig.objects.create(
            empid=employee,
            desigid_id=request.POST.get('designation'),
            from_date=request.POST.get('joindate'),

        )

        # Handle empdpt
        empdpt.objects.create(
            empid=employee,
            dptid_id=request.POST.get('department'),
            from_date=request.POST.get('joindate'),
        
        )

        # Handle salary
        salary.objects.create(
            empid=employee,
            salary=request.POST.get('salary'),
            from_date=request.POST.get('joindate'),
        )

        # Handle scd
        class_ids = request.POST.getlist('classids')
        division_ids = request.POST.getlist('divisionids')
        subject_ids = request.POST.getlist('subjectids')

        print(class_ids,subject_ids,division_ids)
   
        for class_id, division_id, subject_id in zip(class_ids, division_ids, subject_ids):
            
          
            class_instance = get_object_or_404(Academicclass, pk=int(class_id))
            division_instance=get_object_or_404(Academicdivision, pk=int(division_id))
            subject_instance=get_object_or_404(AcademicSubject, pk=int(subject_id))
            scd_instance = scd(
            empid=employee,
            classid_id=class_id,
            divid_id=division_id,
            subid_id=subject_id,
            )
            scd_instance.save()
            
        """ scd.objects.create(
                empid=employee,
                classid_id= class_instance ,
                divid_id= division_instance,
                subid_id=subject_instance,
            )"""

    context={
        'qualification_data':qualif,
        'designation_data':emp,
        'department_data':dept,
        'employee_data':ademp,
        'class_data':cls,
        'division_data':div,
        'subject_data':sub,
        

    }
    
    return render(request,'admin_emp_add.html',context)

def get_subjects_for_class(request):
    class_id = request.GET.get('class_id')
    
    subjects = SubjectFore.objects.filter(classid_id=class_id).values('subjectid__id', 'subjectid__subjectclass')
    
    return JsonResponse(list(subjects), safe=False)

def emp_list(request):
     employees  = adminemp.objects.all()
     return render(request, 'admin_emp_list.html',{'employees': employees})
 
def admin_emp_edit(request):
    mob=adminemp.objects.filter(status=1)
    return render(request, 'admin_emp_edit.html',{'mob':mob})
 