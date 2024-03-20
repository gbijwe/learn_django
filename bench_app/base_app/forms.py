from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsers, Resource_info, Resource


ADM = "Admin"
CMP = "Company"
usr_choice = [
    (ADM, "Admin"),
    (CMP, "Company")
]


class UserRegisterForm(UserCreationForm):
    # here only add fields other than default form field like username and password
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUsers
        fields = [
            'username', 'email', 'usr_type', 'password1', 'password2',
        ]
        widgets = {
            'usr_type': forms.RadioSelect(choices=[(ADM, "Admin"), (CMP, "Company")]),
        }
