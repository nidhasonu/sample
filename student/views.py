from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .forms import *
from .models import *
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


from college.models import *
Usermodel = get_user_model()


class student_add(View):
    def get(self, request):
        form = studentform()
        return render(request, 'student/student_page.html', {'form': form})

    def post(self, request):
        form = studentform(request.POST)
        if form.is_valid():
            user_instance = Usermodel.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                user_type='STUDENT'
            )

            student_instance = form.save(commit=False)
            student_instance.login_page = user_instance
            student_instance.save()

            return redirect('vacancy_college')
        else:
            return render(request, 'student/student_page.html', {'form': form})

class college_vacancy(View):
    def get(self,request):
        return render(request,"student/college_vacancy.html")


class vacancy_view(View):
    def get(self,request):
        view = collegemodel.objects.all()
        return render(request,"student/vacancy_view.html",{'data':view})

class details_view(View):
        def get(self, request, id):
            viewed = homeview.objects.get(pk=id)
            return render(request, "student/national_college.html", {'data': viewed})

            def post(self, request, id):
                view_college = homeview.objects.get(pk=id)
                view_form = homeform(request.POST, instance=view_college)
                if view_form.is_valid():
                    view_form.save()
                    return redirect('view_college')
                return render(request, "student/national_college.html")


class addmission_views(View):
    def get(self,request):
        view_addmission = Addmission_details.objects.all()
        return render(request,"student/addmission_view.html",{'data':view_addmission})


class natonal(View):
    def get(self,request):
        views=homeview.objects.all()
        return render(request,"student/national_college.html",{'data':views})


class maharajas(View):
    def get(self, request):
        return render(request, "student/maharaj_college.html")



class request_send(View):
    def get(self,request):
        return render(request,"student/request_status.html")



class AddFeedback(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'student/feedback.html')
    
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedbacks_view')
        return render(request, 'student/feedback.html')

class view_feedback(View):
    def get(self,request):
        feedbacks=Feedback.objects.all()
        return render(request,"student/feedback_view.html",{'view':feedbacks})

class edit_feedback(View):
    def get(self,request,id):
        edited=Feedback.objects.get(pk=id)
        return render(request, "student/feedback_edit.html", {'edited': edited})

        def post(self, request, id):
            edit_feedbacks = Feedback.objects.get(pk=id)
            edit_form = FeedbackForm(request.POST, instance=edit_feedbacks)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('feedbacks_view')
            return render(request, "student/feedback_edit.html")

class feedback_delt(View):
    def get(self, request, id):
        delet_feedback = Feedback.objects.get(pk=id)
        return render(request, "college/college_home_delet.html")

    def post(self, request, id):
        delet_feedback = Feedback.objects.get(pk=id)
        delet_feedback.delete()
        return redirect('feedbacks_view')





def send_request_view(request):
    if request.method == 'POST':
        form = SeatTransferRequestForm(request.POST)
        if form.is_valid():
            request_form = form.save(commit=False)
            request_form.student = request.user
            request_form.save()
            return redirect('view_requests')
    else:
        form = SeatTransferRequestForm()
    return render(request, 'student/send_request.html', {'form': form})


def view_request_status_view(request):
    requests = SeatTransferRequest.objects.filter(student=request.user)
    return render(request, 'student/view_requests.html', {'requests': requests})


















