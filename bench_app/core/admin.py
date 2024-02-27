from django.contrib import admin
from .models import Users, Company, Resource_Type, Resource
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.forms import UserRegisterForm
from .models import Users

# admin.site.register(Users)
admin.site.register(Company)
admin.site.register(Resource_Type)
admin.site.register(Resource)


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserRegisterForm
    model = Users
    list_display = ["email", "username",]

admin.site.register(Users)