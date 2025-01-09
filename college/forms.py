from django import forms
from .models import *

class collegeform(forms.ModelForm):
    class Meta:
        model=collegemodel
        fields ='__all__'


class NotificationForm(forms.ModelForm):
    class Meta:
        model = ExamNotification
        fields = ['subject', 'notification_content', 'exam_date']


class addmission_form(forms.ModelForm):
    class Meta:
        model = Addmission_details
        fields = '__all__'

class document_form(forms.ModelForm):
    class Meta:
        model = addmission_documents
        fields = '__all__'

class facility_form(forms.ModelForm):
    class Meta:
        model=Facility
        fields = '__all__'

class programme_form(forms.ModelForm):
    class Meta:
        model=programm_notification
        fields = '__all__'

class vacancy_form(forms.ModelForm):
    class Meta:
        model =vacancy
        fields = '__all__'

