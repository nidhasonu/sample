from django.urls import path
from.views import*
from .views import UserLogin
app_name="userapp"

urlpatterns=[
    path('manager/',manager_home_page.as_view(),name="adminpage"),
    path('college/',college_home_page.as_view(),name="collegepage"),
    path('student/',student_home_page.as_view(),name="studentpage"),
    path('loginpages/', UserLogin.as_view(), name='loginpages'),
]


