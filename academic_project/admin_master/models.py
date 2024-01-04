from django.db import models

class Academicdepartment (models.Model):
    deptname=models.CharField(max_length=260)
    deptcode=models.CharField(max_length=260)
    deptstatus=models.IntegerField(default=1)
    
class Academicclass(models.Model):
    classname = models.CharField(max_length=260)
    classstatus = models.IntegerField(default=1)
     
class Academicdesignation(models.Model):
    designame = models.CharField(max_length=260)
    desigcode = models.CharField(max_length=260)
    desigstatus = models.IntegerField(default=1)
 
class Academicqualification(models.Model):
    qualificationname = models.CharField(max_length=260)
    qualificationstatus = models.IntegerField(default=1)
  
class Academicdivision(models.Model):
    divisionname = models.CharField(max_length=260)
    divisionstatus = models.IntegerField(default=1)  
      
class Academicemployee(models.Model):    
    EMPLOYEE_TYPE_CHOICES=[
        (1,'Accountant'),
        (2,'Teacher'),
        (3,'Mess'),
        (4,'Librarian'),
        (5,'other'),
        
    ]
    
    employee_cat_name =  models.CharField(max_length=260)
    employee_cat_area = models.IntegerField(choices=EMPLOYEE_TYPE_CHOICES)
    employee_cat_status=models.IntegerField(default=1)
    
        
       
# Create your models here.

