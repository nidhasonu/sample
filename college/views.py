from django.shortcuts import render, redirect, get_object_or_404
from .models import collegemodel
from .forms import *
from django.views import View
from django.http import HttpResponse
from .models import *
from student. models import studentmodel
from django.contrib import messages
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
        def get(self, request):
            return render(request, 'college/notification.html')

        def post(self, request):
            if 'login_id' not in request.session:
                messages.error(request, 'Session expired. Please log in again.')
                return redirect('userapp:loginpages')
            try:
                print("session id ------------------------>", request.session['login_id'])
                login = Usermodel.objects.get(id=request.session['login_id'])
                print("login-------------------->",login)
                college = collegemodel.objects.filter(user_pages_id=login)
                print("college------------->",college)
                if not college:
                    messages.error(request, 'You are not authorized to upload notification')
                    return redirect('userapp:loginpages')
            except Usermodel.DoesNotExist:
                messages.error(request, 'Invalid session. Please log in again.')
                return redirect('userapp:loginpages')
            picture = NotificationForm(request.POST, request.FILES)
            if picture.is_valid():
                c = picture.save(commit=False)
                c.lock = collegemodel.objects.get(user_pages_id=login)
                c.connect = login
                c.save()
                messages.success(request, 'notification successfully.')
                return redirect('notification_view')
            else:
                messages.error(request, 'Unable . Please try again.')
            return render(request, 'college/notification.html')


class notification_views(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = ExamNotification.objects.filter(connect=content)
        except Usermodel.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, "college/notification_view.html",{'data':content_media})



class notification_edit(View):
        def get(self, request, id):
            items = get_object_or_404(ExamNotification, pk=id)
            return render(request, 'college/notification_editing.html', {'editings': items})

        def post(self, request, id):
            items = get_object_or_404(ExamNotification, pk=id)
            item = NotificationForm(request.POST, request.FILES, instance=items)
            if item.is_valid():
                data = item.save(commit=False)
                data.connect = Usermodel.objects.get(id=request.session['login_id'])
                data.save()
                messages.success(request, 'notification edited')
                return redirect('notification_view')
            return render(request, 'college/notification_editing.html', {'editings': items})



class notification_delete(View):
    def get(self,request,id):
        deleting=ExamNotification.objects.get(pk=id)
        return render(request,"college/notification_delete.html")
    def post(self,request,id):
        notificat_delet=ExamNotification.objects.get(pk=id)
        notificat_delet.delete()
        return redirect('notification_view')


class addmission_add(View):
        def get(self, request):
            return render(request, 'college/addmission_add.html')

        def post(self, request):
            if 'login_id' not in request.session:
                messages.error(request, 'Session expired. Please log in again.')
                return redirect('userapp:loginpages')
            try:
                print("session id ------------------------>", request.session['login_id'])
                login = Usermodel.objects.get(id=request.session['login_id'])
                print("login-------------------->", login)
                college = collegemodel.objects.filter(user_pages_id=login)
                print("college------------->", college)
                if not college:
                    messages.error(request, 'You are not authorized to upload admissions')
                    return redirect('userapp:loginpages')
            except Usermodel.DoesNotExist:
                messages.error(request, 'Invalid session. Please log in again.')
                return redirect('userapp:loginpages')
            add = addmission_form(request.POST, request.FILES)
            if add.is_valid():
                all = add.save(commit=False)
                all.lock = collegemodel.objects.get(user_pages_id=login)
                all.connect = login
                all.save()
                messages.success(request, 'addmission successfully.')
                return redirect('view_addmission')
            else:
                messages.error(request, 'Unable . Please try again.')
            return render(request, 'college/addmission_add.html')


class addmission_view(View):
      def get(self, request):
        try:
            contain = request.session.get('login_id')
            content_media = Addmission_details.objects.filter(connect=contain)
        except Usermodel.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, "college/addmission_view.html", {'data': content_media})


class addmission_edit(View):
    def get(self, request, id):
        edit_addmission = get_object_or_404(Addmission_details, pk=id)
        return render(request, 'college/addmission_edit.html', {'edited': edit_addmission})

    def post(self, request, id):
        Edited = get_object_or_404(Addmission_details, pk=id)
        edit_form = addmission_form(request.POST, request.FILES, instance=Edited)
        if edit_form.is_valid():
            data = edit_form.save(commit=False)
            data.connect = Usermodel.objects.get(id=request.session['login_id'])
            data.save()
            messages.success(request, 'notification edited')
            return redirect('view_addmission')
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
    def get(self, request):
        return render(request, 'college/documents_add.html')

    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('userapp:loginpages')
        try:
            print("session id ------------------------>", request.session['login_id'])
            login = Usermodel.objects.get(id=request.session['login_id'])
            print("login-------------------->", login)
            college = collegemodel.objects.filter(user_pages_id=login)
            print("college------------->", college)
            if not college:
                messages.error(request, 'You are not authorized to upload admissions')
                return redirect('userapp:loginpages')
        except Usermodel.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('userapp:loginpages')
        add = document_form(request.POST, request.FILES)
        if add.is_valid():
            all = add.save(commit=False)
            all.lock = collegemodel.objects.get(user_pages_id=login)
            all.connect = login
            all.save()
            messages.success(request, 'addmission successfully.')
            return redirect('document_view')
        else:
            messages.error(request, 'Unable . Please try again.')
        return render(request, 'college/documents_add.html')


class document_view(View):
    def get(self, request):
        try:
            contain = request.session.get('login_id')
            content_media = addmission_documents.objects.filter(connect=contain)
        except Usermodel.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, "college/document_view.html", {'document': content_media})


class document_edit(View):
    def get(self, request, id):
        edit_document = get_object_or_404(addmission_documents, pk=id)
        return render(request, 'college/document_edit.html', {'data': edit_document})

    def post(self, request, id):
        edited_document = get_object_or_404(addmission_documents, pk=id)
        edit_form = document_form(request.POST, request.FILES, instance=edited_document)
        if edit_form.is_valid():
            datas = edit_form.save(commit=False)
            datas.connect = Usermodel.objects.get(id=request.session['login_id'])
            datas.save()
            messages.success(request, 'document edited')
            return redirect('document_view')
        return render(request,"college/document_view.html",{'edited':edited_document})



class document_delete(View):
    def get(self,request,id):
        deleted = addmission_documents.objects.get(pk=id)
        return render(request, "college/document_dellte.html")

    def post(self, request, id):
        document_delet = addmission_documents.objects.get(pk=id)
        document_delet.delete()
        return redirect('document_view')


class college_facilites(View):
    def get(self, request):
        return render(request, 'college/facility_add.html')

    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('userapp:loginpages')
        try:
            print("session id ------------------------>", request.session['login_id'])
            login = Usermodel.objects.get(id=request.session['login_id'])
            print("login-------------------->", login)
            college = collegemodel.objects.filter(user_pages_id=login)
            print("college------------->", college)
            if not college:
                messages.error(request, 'You are not authorized to upload admissions')
                return redirect('userapp:loginpages')
        except Usermodel.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('userapp:loginpages')
        add = facility_form(request.POST, request.FILES)
        if add.is_valid():
            all = add.save(commit=False)
            all.lock = collegemodel.objects.get(user_pages_id=login)
            all.connect = login
            all.save()
            messages.success(request, 'addmission successfully.')
            return redirect('view_facility')
        else:
            messages.error(request, 'Unable . Please try again.')
        return render(request, 'college/facility_add.html')


class facility_view(View):
    def get(self,request):
        try:
            contain = request.session.get('login_id')
            content_media = Facility.objects.filter(connect=contain)
        except Usermodel.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, "college/facility_view.html",{'data':content_media})


class facility_editing(View):
    def get(self, request, id):
        edit_facility = get_object_or_404(Facility, pk=id)
        return render(request, 'college/facility_edit.html', {'facility': edit_facility})

    def post(self, request, id):
        facility_edit = get_object_or_404(Facility, pk=id)
        form_facility = facility_form(request.POST, request.FILES, instance=facility_edit)
        if form_facility.is_valid():
            datas = form_facility.save(commit=False)
            datas.connect = Usermodel.objects.get(id=request.session['login_id'])
            datas.save()
            messages.success(request, 'facility edited')
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
    def get(self, request):
        try:
            view_programme = request.session.get('login_id')
            content_media = programm_notification.objects.filter(connect=view_programme)
        except Usermodel.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, "college/programme_view.html", {'details': content_media})


class programme_edit(View):
            def get(self, request, id):
                edit_programme = get_object_or_404(programm_notification, pk=id)
                return render(request, 'college/programme_edit.html', {'programme': edit_programme})

            def post(self, request, id):
                progarme_id = get_object_or_404(programm_notification, pk=id)
                programme_forms = programme_form(request.POST, request.FILES, instance=progarme_id)
                if programme_forms.is_valid():
                    datas = programme_forms.save(commit=False)
                    datas.connect = Usermodel.objects.get(id=request.session['login_id'])
                    datas.save()
                    messages.success(request, 'programmes edited')
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


class view_std(View):
    def get(self,request):
        student_view = studentmodel.objects.all()
        return render(request,"college/student_views.html",{'data':student_view})

class home(View):
    def get(self,request):
        home_page=collegemodel.objects.all()
        return render(request,"college/college_home_view.html",{'data':home_page})

class add(View):
    def get(self,request):
        return render(request,"college/college_home_add.html")
    def post(self,request):
        add_home=collegeform(request.POST,request.FILES)
        if add_home.is_valid():
            add_home.save()
            return redirect('Home_view')
        return render(request,"college/college_home_add.html")

class home_edit(View):
    def get(self,request,id):
        home_edit = get_object_or_404(collegemodel, pk=id)
        return render(request, 'college/college_home_edit.html', {'details': home_edit})

def post(self,request,id):
    edit_home = get_object_or_404(collegemodel, pk=id)
    edit_form =collegeform(request.POST,request.FILES,instance=edit_home)
    if edit_form.is_valid():
        datas = edit_form.save(commit=False)
        datas.connect = Usermodel.objects.get(id=request.session['login_id'])
        datas.save()
        messages.success(request, 'homepage edited')
        return redirect('Home_view')
        return render(request, "college/college_home_edit.html", {'details': edit_form})


class home_delt(View):
    def get(self,request,id):
        delet_home = collegemodel.objects.get(pk=id)
        return render(request,"college/college_home_delet.html")

    def post(self, request, id):
        delet_card = collegemodel.objects.get(pk=id)
        delet_card.delete()
        return redirect('Home_view')


class college_home(View):
    def get(self,request):
       return render(request,"college/college_page.html")

class add_vacancy(View):
    def get(self,request):
        return render(request,"college/course_vacancy.html")
    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('userapp:loginpages')
        try:
            print("session id ------------------------>", request.session['login_id'])
            login = Usermodel.objects.get(id=request.session['login_id'])
            print("login-------------------->", login)
            college = collegemodel.objects.filter(user_pages_id=login)
            print("college------------->", college)
            if not college:
                messages.error(request, 'You are not authorized to upload notification')
                return redirect('userapp:loginpages')
        except Usermodel.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('userapp:loginpages')
        vacancy = vacancy_form(request.POST, request.FILES)
        if vacancy.is_valid():
            c = vacancy.save(commit=False)
            c.lock = collegemodel.objects.get(user_pages_id=login)
            c.connect = login
            c.save()
            messages.success(request, 'vacancy successfully.')
            return redirect('college:vacancy_course')
        else:
            messages.error(request, 'Unable . Please try again.')
        return render(request, 'college/course_vacancy.html')


class view_coure(View):
    def get(self, request):
        try:
            view_coure = request.session.get('login_id')
            content_media = vacancy.objects.filter(connect=view_coure)
        except Usermodel.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, "college/cours_view.html", {'vacancys': content_media})


class vacancy_edit(View):
    def get(self,request,id):
        edit_vacany = get_object_or_404(vacancy, pk=id)
        return render(request, 'college/edit_vacancy.html', {'editing': edit_vacany})

    def post(self, request, id):
        vacancy_edite = get_object_or_404(vacancy, pk=id)
        form_vacancy = vacancy_form(request.POST, request.FILES, instance=vacancy_edite)
        if form_vacancy.is_valid():
            edited = form_vacancy.save(commit=False)
            edited.connect = Usermodel.objects.get(id=request.session['login_id'])
            edited.save()
            messages.success(request, 'vacancy edited')
            return redirect('college:vacancy_course')
            return render(request, "college/edit_vacancy.html", {'editing': form_vacancy})

class VacancyDeleteView(View):
    def get(self, request, id):
        vacancy_to_delete = get_object_or_404(vacancy, pk=id)
        return render(request, "college/delet_vacancy.html")

    def post(self, request, id):
        vacancy_to_delete = get_object_or_404(vacancy, pk=id)
        vacancy_to_delete.delete()
        return redirect('college:vacancy_course')
    

class about_add(View):
    def get(self,request):
        return render(request,"college/about.html")
    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('userapp:loginpages')
        try:
            print("session id ------------------------>", request.session['login_id'])
            login = Usermodel.objects.get(id=request.session['login_id'])
            print("login-------------------->", login)
            college = collegemodel.objects.filter(user_pages_id=login)
            print("college------------->", college)
            if not college:
                messages.error(request, 'You are not authorized to upload discripition')
                return redirect('userapp:loginpages')
        except Usermodel.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('userapp:loginpages')
        about = about_form(request.POST, request.FILES)

        if about.is_valid():
            c = about.save(commit=False)
            c.lock = collegemodel.objects.get(user_pages_id=login)
            c.connect = login
            c.save()
            messages.success(request, 'details successfully.')
            return HttpResponse('send')
        else:
            messages.error(request, 'Unable . Please try again.')
        return render(request, 'college/about.html')

















