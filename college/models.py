from django.db import models
from django.template.defaultfilters import default
from userapp.models import *
# Create your models here.

class collegemodel(models.Model):
    user_pages = models.OneToOneField(Usermodel, on_delete=models.CASCADE,null=True,blank=True)
    college_image=models.ImageField(null=True,blank=True,upload_to="images")
    college_name=models.CharField(max_length=30,null=True,blank=True)
    College_code=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=20,null=True,blank=True)
    Contact_number=models.IntegerField(null=True,blank=True)
    Address=models.CharField(max_length=25,null=True,blank=True)
    City=models.CharField(max_length=20,null=True,blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class ExamNotification(models.Model):
    subject = models.CharField(max_length=100, null=True, blank=True)
    connect=models.ForeignKey(Usermodel,on_delete=models.CASCADE,null=True,blank=True)
    lock=models.ForeignKey(collegemodel,on_delete=models.CASCADE, null=True, blank=True)
    notification_content = models.TextField(null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    notification_sent = models.DateTimeField(null=True, blank=True)
    status = models.CharField(default="active", max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)




class Addmission_details(models.Model):
    connect = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True, blank=True)
    lock = models.ForeignKey(collegemodel, on_delete=models.CASCADE, null=True, blank=True)
    college_name = models.CharField(max_length=30, null=True, blank=True)
    Eligibility=models.CharField(max_length=30,null=True,blank=True)
    Subject=models.CharField(max_length=20,null=True,blank=True)
    Addmission_start_date = models.DateField(null=True, blank=True)
    Addmission_end_date = models.DateField(null=True, blank=True)


class addmission_documents(models.Model):
    connect = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True, blank=True)
    lock = models.ForeignKey(collegemodel, on_delete=models.CASCADE, null=True, blank=True)
    Sslc_certificate=models.FileField(null=True,blank=True,upload_to="Files/")
    Plustwo_certificate=models.FileField(null=True,blank=True,upload_to="Files/")
    ID_card=models.FileField(null=True,blank=True,upload_to="Files/")
    TC=models.FileField(null=True,blank=True,upload_to="Files/")
    CC=models.FileField(null=True,blank=True,upload_to="Files/")


class Facility(models.Model):
    connect = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True, blank=True)
    lock = models.ForeignKey(collegemodel, on_delete=models.CASCADE, null=True, blank=True)
    Name=models.CharField(max_length=20,null=True,blank=True)
    Description=models.CharField(max_length=40,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to="facility/")


class programm_notification(models.Model):
    connect = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True, blank=True)
    lock = models.ForeignKey(collegemodel, on_delete=models.CASCADE, null=True, blank=True)
    Titel=models.CharField(max_length=25,null=True,blank=True)
    Venue=models.CharField(max_length=25,null=True,blank=True)
    Start_date=models.DateTimeField(null=True,blank=True)
    End_date=models.DateTimeField(null=True,blank=True)



class vacancy(models.Model):
    connect = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True, blank=True)
    lock = models.ForeignKey(collegemodel, on_delete=models.CASCADE, null=True, blank=True)
    Programme = models.CharField(max_length=30,null=True,blank=True)
    Totel_Seat = models.IntegerField(null=True,blank=True)
    Availbale_Seat =models.IntegerField(null=True,blank=True)
    Dead_line=models.DateField(null=True,blank=True)


class about(models.Model):
    title = models.CharField(max_length=140,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    teammember1=models.CharField(max_length=120,null=True,blank=True)
    teammember2= models.CharField(max_length=120,null=True,blank=True)
    teamimg1 = models.ImageField(upload_to='team_images/', null=True, blank=True)
    teamimg2 = models.ImageField(upload_to='team_images/', null=True, blank=True)
    teamimg3 = models.ImageField(upload_to='team_images/', null=True, blank=True)
    camimg1=models.ImageField(upload_to='images/', null=True, blank=True)
    camimg2 = models.ImageField(upload_to='images/', null=True, blank=True)
    camimg3 = models.ImageField(upload_to='images/', null=True, blank=True)
    connect = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True, blank=True)
    lock = models.ForeignKey(collegemodel, on_delete=models.CASCADE, null=True, blank=True)





















