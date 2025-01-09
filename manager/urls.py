from django.urls import path
from .views import *




urlpatterns=[
    path('view_std/', student_view.as_view(), name="view_std"),
    path('admin_panal/',admin_page.as_view(),name="admin_panal"),
    path('view_complint/',riply.as_view(),name="view_complint"),
    path('coures/',course_college.as_view(),name="coures"),
    path('feedback/',view_feedback.as_view(),name="feedback"),
    path('verify/',Verify.as_view(),name="verify"),
    path('verification/<int:id>',Verify.as_view(),name="verification")


]