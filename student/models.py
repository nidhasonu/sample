from django.db import models
from userapp.models import Usermodel
from django.contrib.auth.models import User
from datetime import datetime
from college.models import *


class studentmodel(models.Model):
    Gender_choices = [
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('OTHER', 'other')
    ]

    university_under = [
        ('CENTER', 'center'),
        ('CALICUT', 'calicut'),
        ('COCHIN', 'cochin'),
        ('NATIONAL', 'national')
    ]

    Name = models.CharField(max_length=25, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Date_of_birth = models.DateField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Father_name = models.CharField(max_length=20, null=True, blank=True)
    login_page = models.OneToOneField(Usermodel, on_delete=models.CASCADE, null=True, blank=True)
    Mother_name = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=Gender_choices)
    City = models.CharField(max_length=20, null=True, blank=True)
    Ph_num = models.IntegerField(null=True, blank=True)
    Addar_num = models.IntegerField(null=True, blank=True)
    Qualification = models.CharField(max_length=20, null=True, blank=True)
    University = models.CharField(max_length=20, null=True, blank=True, choices=university_under)
    status = models.CharField(default="active", max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)



class Feedback(models.Model):
    desciption=models.CharField(max_length=30,null=True,blank=True)
    titel=models.CharField(max_length=30,null=True,blank=True)
    status = models.CharField(default="active", max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)




class SeatTransferRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('SEAT', 'Seat Request'),
        ('TRANSFER', 'Transfer Request'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    student = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True,blank=True)
    college = models.ForeignKey(collegemodel, on_delete=models.CASCADE)
    program = models.ForeignKey(vacancy, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    date_submitted = models.DateTimeField(default=datetime.now)
    reason = models.TextField(blank=True, null=True)



class College(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()


class Review(models.Model):
    college = models.ForeignKey(collegemodel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Usermodel, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)














