from django.urls import path
from.views import*


urlpatterns=[
    path('students/',student_add.as_view(),name="students"),
    path('vacancy_college/',college_vacancy.as_view(),name="vacancy_college"),
    path('addmission_view/',addmission_views.as_view(),name="addmission_view"),
    path('vacancy_view/',vacancy_view.as_view(),name="vacancy_view"),
    path('view<int:id>/',natonal.as_view(),name="view"),
    path('maharaj/',maharajas.as_view(),name="maharaj"),
    path('request_sends/',request_send.as_view(),name="request_sends"),
    path('add-feedback/', AddFeedback.as_view(), name='add-feedback'),
    path('feedbacks_view/',view_feedback.as_view(),name="feedbacks_view"),
    path('feedback_edit/<int:id>',edit_feedback.as_view(),name="feedback_edit"),
    path('feedback_delt/<int:id>',feedback_delt.as_view(),name="feedback_delt"),
    path('view_college/<int:id>',details_view.as_view(),name="view_college"),
    path('send-request/',send_request_view, name='send_request'),
    path('view-requests/', view_request_status_view, name='view_requests'),


]






