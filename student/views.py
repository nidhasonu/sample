from django.db.models.query_utils import select_related_descend
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .forms import *
from .models import *
from django.urls import reverse
from django.contrib import messages
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



class Submitreview(View):
    def get(self, request):
        return render(request, 'student/submitt_review.html')

    def post(self, request):
        user_id = request.session.get('login_id')
        if not user_id:
            return redirect('userapp:loginpages')

        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if rating:
            review.objects.create(
                user_id=user_id,rating=int(rating),comment=comment
            )
            return HttpResponse(f"<script>alert('Thank you for the feedback and rating'); window.location.href='/public/userpage/';</script>")
        return render(request, 'student/submitt_review.html', {'error': 'Please select a rating.'})



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
        return render(request, "student/feedback_delt.html")

    def post(self, request, id):
        delet_feedback = Feedback.objects.get(pk=id)
        delet_feedback.delete()
        return redirect('student:feedbacks_view')

class SendRequestView(View):
    def get(self,request):
           return render(request,"student/send_request.html")

    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('userapp:loginpages')
        try:
            print("session id ------------------------>", request.session['login_id'])
            login = Usermodel.objects.get(id=request.session['login_id'])
            print("login-------------------->", login)
            student = collegemodel.objects.filter(user_pages_id=login)
            print("college------------->", student)
            if not student:
                messages.error(request, 'You are not authorized to upload request')
                return redirect('userapp:loginpages')
        except Usermodel.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('userapp:loginpages')
        requested = SeatTransferRequestForm(request.POST, request.FILES)
        if requested.is_valid():
            c = requested.save(commit=False)
            c.lock = collegemodel.objects.get(user_pages_id=login)
            c.connect = login
            c.save()
            messages.success(request, 'vacancy successfully.')
            return redirect('view_requests')
        else:
            messages.error(request, 'Unable . Please try again.')
        return render(request,'student/send_request.html',{'det':data,'notification':vacancy})



class view_request(View):
    def get(self, request):
        college = get_object_or_404(collegemodel)
        requests = SeatTransferRequest.objects.filter(college=college)
        return render(request, "student/view_requests.html", {'requests': requests})





class ViewColleges(View):
    def get(self, request, id):
        card_college = collegemodel.objects.get(pk=id)
        notifications = card_college.examnotification_set.all()
        abouts=card_college.about_set.all()
        return render(request, 'student/college_view.html', {
            'det': card_college,
            'notifications': notifications,

        })




class about_view(View):
        def get(self, request,id):
            college = get_object_or_404(collegemodel, pk=id)
            aboutss = about.objects.filter(lock=college)
            return render(request, "student/about.html",{'data':aboutss,'team':aboutss})



class NotificationView(View):
    def get(self, request, id):
        college = get_object_or_404(collegemodel, pk=id)
        notifications = ExamNotification.objects.filter(lock=college)
        return render(request, "student/notifications.html", {'college': college, 'notifications': notifications})

class ProgrammeView(View):
    def get(self,request,id):
        college= get_object_or_404(collegemodel,pk=id)
        notification = programm_notification.objects.filter(lock=college)
        return render(request,"student/prgme_notifictin.html",{ 'progrmme': notification})

class Facilitys(View):
    def get(self, request, id):
        college = get_object_or_404(collegemodel, pk=id)
        viewFacility = Facility.objects.filter(lock=college)
        return render(request, "student/Facility_view.html", { 'facility': viewFacility})


class Addmissions(View):
    def get(self, request, id):
        college = get_object_or_404(collegemodel, pk=id)
        admission_details = Addmission_details.objects.filter(lock=college)
        admission_documents = addmission_documents.objects.filter(lock=college)
        context = {
            'admission_details': admission_details,
            'doc': admission_documents
        }
        return render(request, "student/addmission_view.html", context)


class SubmitComplaintView(View):
    def get(self, request, *args, **kwargs):
        form = ComplaintForm()
        return render(request, 'student/complaints.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if 'login_id' not in request.session:
            return redirect('userapp:loginpages')
        user_id = request.session['login_id']
        user = get_object_or_404(Usermodel, id=user_id)

        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.sender = user
            complaint.save()
            return HttpResponse(
                '<script>alert("Complaint submitted successfully!"); window.location.href="/homepage/";</script>')
        return render(request, 'student/complaints.html')

class riplyed(View):
    def get(self,request,id):
        college = get_object_or_404(collegemodel, pk=id)
        ripls = Complaint.objects.filter(lock=college)
        return render(request,"student/view_riply.html")





