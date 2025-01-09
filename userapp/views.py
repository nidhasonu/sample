from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
import json
import datetime

# Create your views here.
class manager_home_page(View):
    def get(self,request):
        return render(request,'manager/admin_panal.html')
class college_home_page(View):
    def get(self,request):
        return render(request,'college/college_page.html')
class student_home_page(View):
    def get(self,request):
        return render(request,'student/college_vacancy.html')
class UserLogin(View):
    template_name ="userapp/login.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
            "ADMIN": "userapp:adminpage",
            "STUDENT": "userapp:studentpage",
            "COLLEGE": "userapp:collegepage",
        }
        username = request.POST.get("username")
        password = request.POST.get("password")
        authenticated = authenticate(username=username, password=password)
        try:
                user = Usermodel.objects.get(username=username)
                request.session['login_id'] = user.id
                if user.status in ["pending", "rejected"] and user.user_type in ["COLLEGE"]:
                    response_dict[
                        "reason"] = f"your {user.user_type.lower()} account status is {user.status}."
                    messages.error(request, response_dict["reason"])
                    return render(request, 'userapp/login.html', {"error_message": response_dict["reason"]})
        except Usermodel.DoesNotExist:
            response_dict[
                "reason"
            ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])

        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return redirect(request.GET.get("from") or "userapp:user")

        else:

            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                user=user, defaults={"session_dict": json.dumps(session_dict)}
            )

            user_type = authenticated.user_type

            request.session["data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "status": user.is_active,
            }
            request.session["user"] = authenticated.username
            request.session["token"] = token.key
            request.session["status"] = user.is_active
            return redirect(landing_page_url[user_type])
        return redirect(request.GET.get("from") or loadlogin)


