from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
  
def admin_department_manage(request):
    success_message=None
    error_message = None
    departments = Academicdepartment.objects.all()
    if request.method == 'POST':
        deptname = request.POST.get('deptname').strip()
        deptcode = request.POST.get('deptcode').strip()
        
        if not deptname or not deptcode:
            # messages.error(request, 'Department name cannot be blank.')
            error_message ='Both Department Name and Code are required.'
        elif Academicdepartment.objects.filter(deptname=deptname).exists():
             error_message='Department Name already exists.'
        elif Academicdepartment.objects.filter(deptcode=deptcode).exists():
             error_message='Department Code already exists.'     
            # messages.error(request, 'Department with this name already exists.')
        else:
            Academicdepartment.objects.create(deptname=deptname, deptcode=deptcode,deptstatus=0)
            success_message='Department added successfully.'
    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'departments': departments,
    }   
    return render(request, 'admin_master_department_manage.html',context)

def edit_dept_ajax(request):
    id=request.GET['id']
    responsedata=Academicdepartment.objects.get(id=id)
    serialized_data={
        'editname':responsedata.deptname,
        'editcode':responsedata.deptcode,
        'editstatus':responsedata.deptstatus,
        
    }
    return JsonResponse(serialized_data)


def update_dept_ajax(request):
    
    if request.method == 'GET':
        id = request.GET['id']
        editname = request.GET['editname']
        editcode = request.GET['editcode']
        editstatus = request.GET['editstatus']

        # Update the department details in the 
        try:
            academic_department = Academicdepartment.objects.get(id=id)
            if Academicdepartment.objects.exclude(id=id).filter(deptname=editname).exists():
                return JsonResponse({'error':"department name already exist",'success':''})
            if Academicdepartment.objects.exclude(id=id).filter(deptcode=editcode).exists():
                return JsonResponse({'error':"department code already exist",'success':''})
            academic_department.deptname = editname
            academic_department.deptcode = editcode
            academic_department.deptstatus = editstatus
            academic_department.save()

            return JsonResponse({'error':'','success': 'Department updated successfully'})
        except Academicdepartment.DoesNotExist:
            return JsonResponse({'error':'Invalid request method','success':''})
        
def delete_dept_ajax(request):
    if request.method=="GET":
        dep_id=request.GET["id"]
        try:
            row=Academicdepartment.objects.get(id=dep_id)
            row.delete()
            return JsonResponse({'success':"row deleted successfully",'error':''})
        except Academicdepartment.DoesNotExist:
            return JsonResponse({'error': 'Invalid id..error 404','success':''}) 
    else:
         return JsonResponse({'error': 'Invalid request..error 404','success':''})            
        
          
def admin_designation_manage(request):
    success_message = None
    error_message = None
    designations = Academicdesignation.objects.all()

    if request.method == 'POST':
        designame = request.POST.get('designame').strip()
        desigcode = request.POST.get('desigcode').strip()

        if not designame or not desigcode:
            error_message = 'Both Designation Name and Code are required.'
        elif Academicdesignation.objects.filter(designame=designame).exists():
            error_message = 'Designation Name already exists.'
        elif Academicdesignation.objects.filter(desigcode=desigcode).exists():
            error_message = 'Designation Code already exists.'
        else:
            Academicdesignation.objects.create(designame=designame, desigcode=desigcode)
            success_message = 'Designation added successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'designations': designations,
    }

    return render(request, 'admin_master_designation_manage.html', context)

def edit_desig_ajax(request):
    id=request.GET['id']
    responsedata=Academicdesignation.objects.get(id=id)
    serialized_data={
        'editname':responsedata.designame,
        'editcode':responsedata.desigcode,
        'editstatus':responsedata.desigstatus,
        
    }
    return JsonResponse(serialized_data)
def update_desig_ajax(request):
    
    if request.method == 'GET':
        id = request.GET['id']
        editname = request.GET['editname']
        editcode = request.GET['editcode']
        editstatus = request.GET['editstatus']

        # Update the department details in the 
        try:
            academic_designation = Academicdesignation.objects.get(id=id)
            if Academicdesignation.objects.exclude(id=id).filter(designame=editname).exists():
                return JsonResponse({'error':"department name already exist",'success':''})
            if Academicdesignation.objects.exclude(id=id).filter(desigcode=editcode).exists():
                return JsonResponse({'error':"department code already exist",'success':''})
            academic_designation.designame = editname
            academic_designation.desigcode = editcode
            academic_designation.desigstatus = editstatus
            academic_designation.save()

            return JsonResponse({'error':'','success': 'Designation updated successfully'})
        except Academicdesignation.DoesNotExist:
            return JsonResponse({'error':'Invalid request method','success':''})
def delete_desig_ajax(request):
    if request.method=="GET":
        des_id=request.GET["id"]
        try:
            row=Academicdesignation.objects.get(id=des_id)
            row.delete()
            return JsonResponse({'success':"row deleted successfully",'error':''})
        except Academicdesignation.DoesNotExist:
            return JsonResponse({'error': 'Invalid id..error 404','success':''}) 
    else:
        return JsonResponse({'error': 'Invalid request..error 404','success':''})           

def admin_qualification_manage(request):
    success_message = None
    error_message = None
    qualifications = Academicqualification.objects.all()

    if request.method == 'POST':
        qualificationname = request.POST.get('qualificationname').strip()
        
        if not qualificationname :
            error_message = 'Qualification Name is required.'
        elif Academicqualification.objects.filter(qualificationname=qualificationname).exists():
            error_message = 'Qualification Name already exists.'
        else:
            Academicqualification.objects.create(qualificationname=qualificationname)
            success_message = 'Qualification added successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'qualifications': qualifications,
    }

    return render(request, 'admin_master_qualification_manage.html', context)
def edit_qualif_ajax(request):
    id=request.GET['id']
    responsedata=Academicqualification.objects.get(id=id)
    serialized_data={
        'editqualname':responsedata.qualificationname,
        'edtqualstat':responsedata.qualificationstatus,
            }
    return JsonResponse(serialized_data)
def update_qualif_ajax(request):
    
    if request.method == 'GET':
        id = request.GET['id']
        editname = request.GET['editname']
        editstatus = request.GET['editstatus']

        # Update the department details in the 
        try:
            academic_qualification = Academicqualification.objects.get(id=id)
            if Academicqualification.objects.exclude(id=id).filter(qualificationname=editname).exists():
                return JsonResponse({'error':"qualification name already exist",'success':''})
            # if Academicqualification.objects.exclude(id=id).filter(desigcode=editcode).exists():
            #     return JsonResponse({'error':"department code already exist",'success':''})
            academic_qualification.qualificationname = editname
            academic_qualification.qualificationstatus = editstatus
            academic_qualification.save()

            return JsonResponse({'error':'','success': 'Designation updated successfully'})
        except Academicqualification.DoesNotExist:
            return JsonResponse({'error':'Invalid request method','success':''})
def delete_qualif_ajax(request):
    if request.method == "GET":
        qua_id=request.GET["id"]
        try:
            row=Academicqualification.objects.get(id=qua_id)
            row.delete()
            return JsonResponse({'success':"row deleted successfully",'error':''})
        except Academicqualification.DoesNotExist:
            return JsonResponse({'error': 'Invalid id..error 404','success':''}) 
    else:
        return JsonResponse({'error': 'Invalid request..error 404','success':''})   
   
def admin_class_manage(request):
    success_message = None
    error_message = None
    classes = Academicclass.objects.all()

    if request.method == 'POST':
        classname = request.POST.get('classname').strip()

        if not classname:
            error_message = 'Class Name is required.'
        elif Academicclass.objects.filter(classname=classname).exists():
            error_message = 'Class Name already exists.'
        else:
            Academicclass.objects.create(classname=classname)
            success_message = 'Class added successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'classes': classes,
    }

    return render(request, 'admin_master_class_manage.html', context)
def edit_class_ajax(request):
    id=request.GET['id']
    responsedata=Academicclass.objects.get(id=id)
    serialized_data={
        'editclassname':responsedata.classname,
        'edtclassstat':responsedata.classstatus,
            }
    return JsonResponse(serialized_data)
def update_class_ajax(request):
    
    if request.method == 'GET':
        id = request.GET['id']
        editname = request.GET['editname']
        editstatus = request.GET['editstatus']

        # Update the department details in the 
        try:
            academic_class = Academicclass.objects.get(id=id)
            if Academicclass.objects.exclude(id=id).filter(classname=editname).exists():
                return JsonResponse({'error':"class name already exist",'success':''})
            # if Academicqualification.objects.exclude(id=id).filter(desigcode=editcode).exists():
            #     return JsonResponse({'error':"department code already exist",'success':''})
            academic_class.classname = editname
            academic_class.classstatus = editstatus
            academic_class.save()

            return JsonResponse({'error':'','success': 'class updated successfully'})
        except Academicclass.DoesNotExist:
            return JsonResponse({'error':'Invalid request method','success':''})
def delete_class_ajax(request):
    if request.method == "GET":
        class_id=request.GET["id"]
        try:
            row=Academicclass.objects.get(id=class_id)
            row.delete()
            return JsonResponse({'success':"row deleted successfully",'error':''})
        except Academicclass.DoesNotExist:
            return JsonResponse({'error': 'Invalid id..error 404','success':''}) 
    else:
        return JsonResponse({'error': 'Invalid request..error 404','success':''})   


def admin_division_manage(request):
    success_message = None
    error_message = None
    divisions = Academicdivision.objects.all()

    if request.method == 'POST':
        divisionname = request.POST.get('divisionname').strip()

        if not divisionname:
            error_message = 'Division Name is required.'
        elif Academicdivision.objects.filter(divisionname=divisionname).exists():
            error_message = 'Division Name already exists.'
        else:
            Academicdivision.objects.create(divisionname=divisionname)
            success_message = 'Division added successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'divisions': divisions
    }

    return render(request, 'admin_master_division_manage.html', context)
def edit_div_ajax(request):
    id=request.GET['id']
    responsedata=Academicdivision.objects.get(id=id)
    serialized_data={
        'editname':responsedata.divisionname,
        # 'editcode':responsedata.deptcode,
        'editstatus':responsedata.divisionstatus,
        
    }
    return JsonResponse(serialized_data)

def update_div_ajax(request):
    
    if request.method == 'GET':
        id = request.GET['id']
        editname = request.GET['editname']
        # editcode = request.GET['editcode']
        editstatus = request.GET['editstatus']

        # Update the department details in the 
        try:
            academic_division = Academicdivision.objects.get(id=id)
            if Academicdivision.objects.exclude(id=id).filter(divisionname=editname).exists():
                return JsonResponse({'error':"division name already exist",'success':''})
            # if Academicdivision.objects.exclude(id=id).filter(deptcode=editcode).exists():
            #     return JsonResponse({'error':"department code already exist",'success':''})
            academic_division.divisionname = editname
            # academic_division.deptcode = editcode
            academic_division.divisionstatus = editstatus
            academic_division.save()

            return JsonResponse({'error':'','success': 'Department updated successfully'})
        except Academicdivision.DoesNotExist:
            return JsonResponse({'error':'Invalid request method','success':''})
        
def delete_div_ajax(request):
    if request.method=="GET":
        div_id=request.GET["id"]
        try:
            row=Academicdivision.objects.get(id=div_id)
            row.delete()
            return JsonResponse({'success':"row deleted successfully",'error':''})
        except Academicdivision.DoesNotExist:
            return JsonResponse({'error': 'Invalid id..error 404','success':''}) 
    else:
         return JsonResponse({'error': 'Invalid request..error 404','success':''})          

def admin_employee_category_manage(request):
    success_message = None
    error_message = None
    Employeecat = Academicemployee.objects.all()
    

    if request.method == 'POST':
        employee_c_name = request.POST.get('empcatname','').strip()
        employee_c_area = request.POST.get('empcatarea','').strip()
        print(type(employee_c_name))

        if not employee_c_name or not employee_c_area :
            error_message = 'both are required.'
        elif Academicemployee.objects.filter(employee_cat_name__iexact=employee_c_name).exists():
            error_message = 'Employee Name already exists.'
        elif Academicemployee.objects.exclude(employee_cat_area=settings.EMPLOYEE_CAT_OTHER).filter(employee_cat_area__iexact=employee_c_area):
            error_message = 'Employee area already exists.'
        else:    
            Academicemployee.objects.create(employee_cat_name=employee_c_name,employee_cat_area=employee_c_area)
            success_message = 'Employee Category added successfully.'

    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'Employeecat': Employeecat,
        'settings':settings
    }

        # return render(request, 'admin_master_division_manage.html', context)
    return render (request, 'admin_master_employee_category_manage.html',context)

def edit_emp_ajax(request):
    id=request.GET['id']
    responsedata=Academicemployee.objects.get(id=id)
    serialized_data={
        'editname':responsedata.employee_cat_name,
        'editcode':responsedata.employee_cat_area,
        'editstatus':responsedata.employee_cat_status,
        
    }
    return JsonResponse(serialized_data)
 # Import your model here

def update_emp_ajax(request):
  if request.method == 'GET':
    try:
        id = request.GET.get('id')
        editname = request.GET.get('editname')
        editcode = request.GET.get('editcode')
        editstatus = request.GET.get('editstatus')

       
        academic_employee = Academicemployee.objects.get(id=id)

            # Check if the updated name already exists (excluding the current employee)
        if not editname:
            return JsonResponse({'error': "cant be blank", 'success': ''})
                
        elif Academicemployee.objects.exclude(id=id).filter(employee_cat_name__iexact=editname).exists():
                error_message = 'Employee Name already exists.'
                return JsonResponse({'error': error_message, 'success': ''})

            # Check if the updated area already exists (excluding the current employee)
        elif not editcode: 
              return JsonResponse({'error': "cant be blank", 'success': ''})  
        elif Academicemployee.objects.exclude(id=id).filter(employee_cat_area=editcode).exclude(employee_cat_area=settings.EMPLOYEE_CAT_OTHER).exists():
                error_message = 'Employee area already exists.'
                return JsonResponse({'error': error_message, 'success': ''})
            
        else:
                success_message = 'Employee Category updated successfully.' 
                academic_employee.employee_cat_name = editname
                academic_employee.employee_cat_area = editcode
                academic_employee.employee_cat_status = editstatus
                academic_employee.save()

                return JsonResponse({'error': '', 'success': success_message})

    except Academicemployee.DoesNotExist:
            return JsonResponse({'error': 'Invalid request method', 'success': ''})
  else:
   return JsonResponse({'error': 'Invalid request method', 'success': ''})

        
def delete_emp_ajax(request):
    if request.method=="GET":
        emp_id=request.GET["id"]
        try:
            row=Academicemployee.objects.get(id=emp_id)
            row.delete()
            return JsonResponse({'success':"row deleted successfully",'error':''})
        except Academicemployee.DoesNotExist:
            return JsonResponse({'error': 'Invalid id..error 404','success':''}) 
    else:
         return JsonResponse({'error': 'Invalid request..error 404','success':''})    
def subject(request):
    success_message=None
    error_message = None
    sub=Academicclass.objects.all()
    subjectcls=AcademicSubject.objects.all()
    if request.method == 'POST':
        selectall= request.POST.getlist('checkboxGroup')
        subject= request.POST.get('subname').strip()
        if not subject:
            # messages.error(request, 'Department name cannot be blank.')
            error_message ='Subject Name is required.'
        elif AcademicSubject.objects.filter(subjectclass=subject).exists():
             error_message='Subject Name already exists.'
        elif not selectall:
             error_message='Select atleast one class'
           
            # messages.error(request, 'Department with this name already exists.')
        else:
            subforeign,foreign=AcademicSubject.objects.get_or_create(subjectclass=subject,subjectstatus=0)
            for clsid in selectall:
              get =  get_object_or_404(Academicclass,pk=int(clsid))
              obj= SubjectFore(classid=get,subjectid=subforeign)
              obj.save()
              success_message='Subject added successfully.'
                
    context = {
        'errormessage': error_message,
        'successmessage': success_message,
        'sub': sub,
        'subjectcls' : subjectcls,
        
    }
    
    return render(request,'subject.html',context)
          
def edit_sub_ajax(request):
    id=request.GET['id']
    responsedata=AcademicSubject.objects.get(id=id)
    serialized_data={
        'editname':responsedata.subjectclass,
        # 'editcode':responsedata.employee_cat_area,
        'editstatus':responsedata.subjectstatus,
    }
    return JsonResponse(serialized_data)
                      

def update_sub_ajax(request):
    
    if request.method == 'GET':
        id = request.GET['id']
        editname = request.GET['editname']
        # editcode = request.GET['editcode']
        editstatus = request.GET['editstatus']

        # Update the department details in the 
        try:
            academic_Subject = AcademicSubject.objects.get(id=id)
            if Academicdepartment.objects.exclude(id=id).filter(subjectclass=editname).exists():
                return JsonResponse({'error':"Subject name already exist",'success':''})
            # if Academicdepartment.objects.exclude(id=id).filter(deptcode=editcode).exists():
            #     return JsonResponse({'error':"department code already exist",'success':''})
            academic_Subject.subjectclass = editname
            # academic_Subject.deptcode = editcode
            academic_Subject.subjectstatus = editstatus
            academic_Subject.save()
            return JsonResponse({'error':'','success': 'Subject updated successfully'})
        except AcademicSubject.DoesNotExist:
            return JsonResponse({'error':'Invalid request method','success':''})
        
                  