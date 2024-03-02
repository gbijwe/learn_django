from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("register/", views.register, name="register"),
    path("land-company", views.myCompany, name="land-company"),
    path("land-admin", views.myAdmin, name="land-admin"),
    path("login/", views.MyLoginView.as_view(template_name="base_app/login.html"), name="login"),
]