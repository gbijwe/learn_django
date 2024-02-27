from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Users

ADM = "Admin"
CMP = "Company"
usr_choice = [
    (ADM, "Admin"),
    (CMP, "Company")
]

class UserRegisterForm(UserCreationForm):
    # here only add fields other than default form field like username and password
    email = forms.EmailField(required=True)
    usr_type = forms.ChoiceField(label="User Type", choices=[(ADM, "Admin"),(CMP, "Company")], required=True)

    class Meta:
        model = Users
        fields = [
            'usr', 'usr_type', 'pswd','company_id',
            # 'username', 'email', 'password1', 'password2', 'usr_type',
        ]