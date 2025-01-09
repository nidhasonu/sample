from.models import Usermodel
from django.contrib.auth.forms import UserChangeForm,UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usermodel
        fields = ("username","password")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usermodel
        exclude = []
