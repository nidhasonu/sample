from django.urls import path
from.views import*



urlpatterns=[
    path('details/',college_add.as_view(),name="details"),
    # path('college_notification/', CollegeNotification.as_view(), name='college_notification'),
    path('notification_view/',notification_views.as_view(),name="notification_view"),
    path('EDIT/<int:id>',notification_edit.as_view(),name="EDIT"),
    path('Deleting/<int:id>',notification_delete.as_view(),name="Deleting"),
    path('add_addmission/',addmission_add.as_view(),name="add_addmission"),
    path('view_addmission/',addmission_view.as_view(),name="view_addmission"),
    path('edit_addmission/<int:id>',addmission_edit.as_view(),name="edit_addmission"),
    path('delete_addmission/<int:id>',addmission_delete.as_view(),name="delete_addmission"),
    path('add_document/',document_add.as_view(),name="add_document"),
    path('document_view/',document_view.as_view(),name="document_view"),
    path('document_edit/<int:id>',document_edit.as_view(),name="document_edit"),
    path('document_delte/<int:id>',document_delete.as_view(),name="document_delte"),
    path('facility_add/',college_facilites.as_view(),name="facility_add"),
    path('view_facility/',facility_view.as_view(),name="view_facility"),
    path('edit_facility/<int:id>',facility_editing.as_view(),name="edit_facility"),
    path('facility_delt/<int:id>',facility_delt.as_view(),name="facility_delt"),
    path('add_programme/',programme_add.as_view(),name="add_programme"),
    path('view_programme/',programme_view.as_view(),name="view_programme"),
    path('edit_progarme/<int:id>',programme_edit.as_view(),name="edit_progarme"),
    path('delt_progrm/<int:id>',programm_delt.as_view(),name="delt_progrm"),
    path('national_college/',national_college.as_view(),name="national_college"),
    path('abouts/',about.as_view(),name="abouts"),
    path('view_student/',view_std.as_view(),name="view_student"),
    path('Home_view/',home.as_view(),name="Home_view"),
    path('home_add/',add.as_view(),name="home_add"),
    path('home_edit/<int:id>',home_edit.as_view(),name="home_edit"),
    path('home_delt/<int:id>',home_delt.as_view(),name="home_delt"),
    path('collegehome/',college_home.as_view(),name="collegehome"),

]
