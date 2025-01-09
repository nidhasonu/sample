from django.shortcuts import render,redirect
from .forms import *
from django.views import View
from django.http import HttpResponse
from .models import *
from student. models import *
from college.models import *
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


# Create your views here.

class student_view(View):
    def get(self,request):
        std_view = studentmodel.objects.all()
        return render(request,"manager/view_student.html",{'view':std_view})

class admin_page(View):
    def get(self,request):
        return render(request,"manager/admin_panal.html")

class riply(View):
    def get(self,request):
        ripl=complaint.objects.all()
        return render(request,"manager/complaint_view.html",{'riplys':ripl})

class course_college(View):
    def get(self,request):
        view_college=collegemodel.objects.all()
        return render(request,"manager/cours_college.html",{'data': view_college})

class view_feedback(View):
    def get(self,request):
        view_feedback = Feedback.objects.all()
        return render(request,"manager/view_feedback.html",{'view':view_feedback})

class Verify(View):
    def get(self,request):
        user_status=Usermodel.objects.filter(user_type='COLLEGE',status='pending')
        return render(request,'manager/varify.html',{'user_status':user_status})
    def post(self,request,id):
        user_data=get_object_or_404(Usermodel,id=id)
        new_status=request.POST.get('status')
        other=['verified','rejected']
        if new_status not in other:
            messages.error(request,"status not changed")
            return redirect('verify')
        user_data.status=new_status
        user_data.save()
        messages.success(request,f"{user_data.username} profile {user_data.status} sucessfully")
        return redirect('verify')








        
