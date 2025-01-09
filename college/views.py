from django.shortcuts import render, redirect
from .models import collegemodel
from .forms import *
from django.views import View
from django.http import HttpResponse
from .models import *
from student. models import studentmodel
# Create your views here.
class college_add(View):
    def get(self, request):
        return render(request,'college/registration.html')

    def post(self, request):
        add = collegeform(request.POST ,request.FILES)
        if add.is_valid():
            alls =add.save(commit=False)
            user = Usermodel.objects.create_user(
                username=request.POST ['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                user_type='COLLEGE'
            )


            alls.user_pages = user
            print(user.email)
            alls.save()

            return redirect('add_addmission')
        else:
            return render(request, 'college/collegedetails.html', {'form': add})


class CollegeNotification(View):
    def get(self, request, college_id):
        """
        Display form for adding a new exam notification and list of existing notifications for the college.
        """
        college = get_object_or_404(CollegeModel, id=college_id)
        form = NotificationForm()
        notifications = ExamNotification.objects.filter(college=college)
        return render(request, 'college/notification.html', {'form': form, 'notifications': notifications, 'college': college})

    def post(self, request, college_id):
        """
        Handle submission of the exam notification form and associate it with the specific college.
        """
        college = get_object_or_404(CollegeModel, id=college_id)
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.college = college
            notification.save()

            return redirect('college_notification', college_id=college.id)
        else:
            notifications = ExamNotification.objects.filter(college=college)
            return render(request, 'college/notification.html', {'form': form, 'notifications': notifications, 'college': college})







class notification_views(View):
    def get(self,request):
        notification=ExamNotification.objects.all()
        return render(request,"college/notification_view.html",{'data':notification})
   
   
class notification_edit(View):
    def get(self,request,id):
        edit=ExamNotification.objects.get(pk=id)
        return render(request,"college/notification_editing.html",{'editings':edit})
    def post(self,request,id):
        edit = ExamNotification.objects.get(pk=id)
        form = NotificationForm(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect("notification_view")
        return render(request, "college/notification_editing.html", {'editings': edit})

class notification_delete(View):
    def get(self,request,id):
        deleting=ExamNotification.objects.get(pk=id)
        return render(request,"college/notification_delete.html")
    def post(self,request,id):
        notificat_delet=ExamNotification.objects.get(pk=id)
        notificat_delet.delete()
        return redirect('notification_view')


class addmission_add(View):
    def get(self,request):
        notificate_add = addmission_form()
        return render(request, 'college/addmission_add.html', {'form': notificate_add})

    def post(self, request):
        form = addmission_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_addmission')
        else:
            return render(request, 'college/addmission_add.html', {'form': form})

class addmission_view(View):
    def get(self,request):
        view_addmission=Addmission_details.objects.all()
        return render(request,"college/addmission_view.html",{'data':view_addmission})

class addmission_edit(View):
    def get(self,request,id):
        edit_addmission=Addmission_details.objects.get(pk=id)
        return render(request,"college/addmission_edit.html",{'edited':edit_addmission})
    def post(self,request,id):
        Edited=Addmission_details.objects.get(pk=id)
        edit_form = addmission_form(request.POST, instance=Edited)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponse("view_addmission")
        return render(request,"college/addmission_edit.html",{'edited':Edited})

class addmission_delete(View):
    def get(self,request,id):
        deleted=Addmission_details.objects.get(pk=id)
        return render(request,"college/addmission_delete.html")
    def post(self,request,id):
        addmission_delet=Addmission_details.objects.get(pk=id)
        addmission_delet.delete()
        return redirect('view_addmission')


class document_add(View):
    def get(self,request):
        return render(request,"college/documents_add.html")
    def post(self,request):
        files = document_form(request.POST,request.FILES)
        if files.is_valid():
            files.save()
            return redirect('document_view')
        return render(request,"college/documents_add.html")

class document_view(View):
    def get(self,request):
        document_file=addmission_documents.objects.all()
        return render(request,"college/document_view.html",{'document':document_file})

class document_edit(View):
    def get(self,request,id):
        edit_document=addmission_documents.objects.get(pk=id)
        return render(request,"college/document_edit.html",{'data':edit_document})
    def post(self,request,id):
        edited_document=addmission_documents.objects.get(pk=id)
        edit_form=document_form(request.POST,request.FILES, instance=edited_document)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('document_view')
        return render(request,"college/document_edit.html",{'data':edit_form})

class document_delete(View):
    def get(self,request,id):
        deleted = addmission_documents.objects.get(pk=id)
        return render(request, "college/document_dellte.html")

    def post(self, request, id):
        document_delet = addmission_documents.objects.get(pk=id)
        document_delet.delete()
        return redirect('document_view')


class college_facilites(View):
    def get(self,request):
        facilites=facility_form()
        return render(request,"college/facility_add.html")
    def post(self,request):
        college_facility=facility_form(request.POST,request.FILES)
        if college_facility.is_valid():
            college_facility.save()
            return redirect('view_facility')
        return render(request,"college/facility_add.html")

class facility_view(View):
    def get(self,request):
        view_facility=Facility.objects.all
        return render(request,"college/facility_view.html",{'data':view_facility})

class facility_editing(View):
    def get(self,request,id):
        edit_facility=Facility.objects.get(pk=id)
        return render(request,"college/facility_edit.html",{'facility':edit_facility})
    def post(self,request,id):
        facility_edit=Facility.objects.get(pk=id)
        form_facility=facility_form(request.POST,request.FILES, instance=facility_edit)
        if form_facility.is_valid():
            form_facility.save()
            return redirect('view_facility')
        return render(request,"college/facility_edit.html",{'facility':form_facility})

class facility_delt(View):
    def get(self,request,id):
        delte_facility=Facility.objects.get(pk=id)
        return render(request,"college/facility_delte.html")
    def post(self,request,id):
        delet_facility = Facility.objects.get(pk=id)
        delet_facility.delete()
        return redirect('view_facility')


class programme_add(View):
    def get(self,request):
        return render(request,"college/prgrm_notification_add.html")
    def post(self,request):
        add_notification=programme_form(request.POST)
        if add_notification.is_valid():
            add_notification.save()
            return redirect('view_programme')
        return render(request,"college/prgrm_notification_add.html")

class programme_view(View):
    def get(self,request):
        view_programme=programm_notification.objects.all
        return render(request,"college/programme_view.html",{'details':view_programme})

class programme_edit(View):
    def get(self,request,id):
        edit_programme=programm_notification.objects.get(pk=id)
        return render(request,"college/programme_edit.html",{'programme':edit_programme})
    def post(self,request,id):
        progarme_id=programm_notification.objects.get(pk=id)
        programme_forms=programme_form(request.POST, instance=progarme_id)
        if programme_forms.is_valid():
            programme_forms.save()
            return redirect('view_programme')
        return render(request,"college/programme_edit.html" ,{'programme':programme_forms})

class programm_delt(View):
    def get(self,request,id):
        delte_progrmm = programm_notification.objects.get(pk=id)
        return render(request, "college/progrmm_delt.html")

    def post(self, request, id):
        delet_pgrm = programm_notification.objects.get(pk=id)
        delet_pgrm.delete()
        return redirect('view_programme')


class national_college(View):
    def get(self,request):
        return render(request,"college/National_university.html")

class about(View):
    def get(self,request):
        return render(request,"college/about.html")

class view_std(View):
    def get(self,request):
        student_view = studentmodel.objects.all()
        return render(request,"college/student_views.html",{'data':student_view})

class home(View):
    def get(self,request):
        home_page=homeview.objects.all()
        return render(request,"college/college_home_view.html",{'data':home_page})

class add(View):
    def get(self,request):
        return render(request,"college/college_home_add.html")
    def post(self,request):
        add_home=homeform(request.POST,request.FILES)
        if add_home.is_valid():
            add_home.save()
            return redirect('Home_view')
        return render(request,"college/college_home_add.html")

class home_edit(View):
    def get(self,request,id):
        home_edit = homeview.objects.get(pk=id)
        return render(request,"college/college_home_edit.html",{'details':home_edit})
    def post(self,request,id):
        edit_home = homeview.objects.get(pk=id)
        edit_form =homeform(request.POST,request.FILES,instance=edit_home)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('Home_view')
        return render(request, "college/college_home_edit.html")

class home_delt(View):
    def get(self,request,id):
        delet_home = homeview.objects.get(pk=id)
        return render(request,"college/college_home_delet.html")

    def post(self, request, id):
        delet_card = homeview.objects.get(pk=id)
        delet_card.delete()
        return redirect('Home_view')


class college_home(View):
    def get(self,request):
       return render(request,"college/college_page.html")

class vacancy_view(View):
    def get(self,request):
        view = collegemodel.objects.all()
        return render(request,"student/vacancy_view.html",{'data':view})

# class vacancy(View):







