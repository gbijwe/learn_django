from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [
    path("", views.Home, name="home"),
    path('register/', user_views.register, name="register"),
    path("myAdmin/", user_views.myAdmin, name='core-admin'),
    path("myCompany/", user_views.myCompany, name='core-company'),
]