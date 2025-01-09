from django.contrib import admin
from .models import *
from userapp.models import (Usermodel,Token,)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {"fields": ("email", "first_name")},
        ),
        (
            _("Permissions"),
            {"fields": ("user_type", "is_active", "is_superuser", "status")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2")},
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("pk","username", "first_name", "user_type")
    search_fields = ("username", "first_name")
    ordering = ("username",)


admin.site.register(Usermodel,CustomUserAdmin)
admin.site.register(Token)



