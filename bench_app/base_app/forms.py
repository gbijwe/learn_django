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
    usr_type = forms.ChoiceField(label="User Type", choices=[(ADM, "Admin"),(CMP, "Company")], required=True)

    class Meta:
        model = CustomUsers
        fields = [
            # 'username', 'usr_type', 'password','company_id',
            'username', 'email', 'usr_type', 'password1', 'password2', 
        ]

# class ResourceInfoForm(forms.ModelForm):
#     class Meta: 
#         model = Resource_info
#         fields = ['resource_type', 'created_by']
#         widgets = {
#             'resource_type': forms.Select(
#                 choices=Resource.objects.values_list('pk', 'resource_type')
#             )
            
#         }
#         def label_from_instance(self, obj):
#             return obj.resource_type_name