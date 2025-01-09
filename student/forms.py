from django import forms
from .models import *

class studentform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = [
            'Name', 'Age', 'Date_of_birth', 'Email', 'Father_name', 'Mother_name',
            'Gender', 'City', 'Ph_num', 'Addar_num', 'Qualification'
        ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class SeatTransferRequestForm(forms.ModelForm):
    class Meta:
        model = SeatTransferRequest
        fields = ['college', 'program', 'request_type', 'reason']




