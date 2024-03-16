from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("land-company/", views.statistics_view, name="land-company"),
    path("land-admin/", views.statistics_view, name="land-admin"),

    # Auth
    path("register/", views.register, name="register"),
    path("login/", views.MyLoginView.as_view(template_name="base_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="base_app/goodbye.html"), name="logout"),

    # Company
    path("land-company/listview/", views.MyListView.as_view(), name="listview"),
    path("land-company/categoryview/", views.CategoryListView.as_view(), name="categoryview"),
    path("land-company/myresources", views.MyResources.as_view(), name="my-resources"),
    path("land-company/<int:category>/", views.MyCategoryView.as_view(), name="categoryview"),
    path("land-company/listview/new", views.MyCreateView.as_view(), name="create-resource"),
    path("land-company/listview/<int:pk>/", views.MyDetailView.as_view(), name="detailview"),
    path("land-company/listview/<int:pk>/update/", views.MyUpdateView.as_view(), name="updateview"),
    path("land-company/listview/<int:pk>/delete", views.MyDeleteView.as_view(), name="deleteview"),
    # path('land-company/<int:category>/book-resource/<int:resource_id>/', views.book_resource, name='book-resource'),
    path('book-resource/<int:resource_id>/', views.book_resource, name='bookresource'),
    path('release-resource/<int:my_id>/', views.release_resource, name='releaseresource'),
    path('land-company/profile/', views.BookingView.as_view(), name="booking-view"),
    # path('land-company/testing/', views.BookingListView.as_view(), name="testing"),


    # Admin 
    path("land-admin/listview/", views.AdminControlListView.as_view(), name="adminlistview"),
    path("land-admin/listview/new", views.AdminCreateTypeView.as_view(), name="create-resource-type"),
    path("land-admin/listview/<int:pk>", views.AdminDetailView.as_view(), name="admindetailview"),
    path("land-admin/listview/<int:pk>/delete/", views.AdminDeleteView.as_view(), name="admindeleteview"),
    path("land-admin/listview/<int:pk>/update/", views.AdminUpdateView.as_view(), name="adminupdateview"),
]