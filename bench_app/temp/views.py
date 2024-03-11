from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView, 
    DeleteView,
    )

from .models import Resource, Resource_info, Booking
import datetime
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator 


def landing_page(request):
    # return HttpResponse("<h3>Welcome to the Bench App.</h3>")
    return render(request, 'base_app/landing.html')

def register(request):
    # creation of a new instance of UserCreationFOrm
    if request.method == 'POST':
        # after creating forms.py, we use UserRegisterForm instead.
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been registered.')
            user_type = form.cleaned_data.get('usr_type')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'base_app/register.html', {'form': form})

# Determine which user goes to which page on login. Admin & company.
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
            """Redirects users based on their type after successful login."""
            user = self.request.user  # Access the authenticated user

            if user.is_authenticated:  # Ensure user is authenticated
                if user.usr_type == "Admin":  # Check for admin type
                    return reverse("land-admin")
                else:
                    return reverse("land-company")
                

            # If user is not authenticated, fall back to the default behavior
            return super().get_success_url()  # Inherit default behavior
    


class AdminHome(LoginRequiredMixin, ListView):
    model = Resource_info
    template_name = 'base_app/home.html'
    context_object_name = 'resources'
    ordering = ['resource_type_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context

class CompanyHome(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'base_app/home.html'
    context_object_name = 'resources'
    ordering = ['resource_type']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context

class MyListView(ListView):
    model = Resource
    template_name = 'base_app/resource_list.html'
    context_object_name = 'resources'
    ordering = ['resource_type']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context

class MyDetailView(DetailView):
    model = Resource
    template_name="base_app/resource_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context

class MyCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    
    fields = [
        'resource_name', 'resource_type', 'description', 'available_date'
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context

class MyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resource
    fields = [
        'resource_name', 'resource_type', 'description'
    ]


    def test_func(self):
        curr_resource = self.get_object()
        if self.request.user == curr_resource.created_by:
            return True
        else: 
            return False 



class MyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resource
    success_url = '/land-company/listview'

    def test_func(self):
        curr_resource = self.get_object()
        if self.request.user == curr_resource.created_by:
            return True
        else: 
            return False 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context
                    

class AdminUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.usr_type == 'Admin'

    def handle_no_permission(self):
        return HttpResponse("You are not an admin")
    

class AdminControlListView(AdminUserMixin, ListView):
    model = Resource_info
    template_name = 'base_app/resource_list.html'
    context_object_name = 'resources'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['usr_type'] = self.request.user.usr_type
        return context


class AdminCreateTypeView(AdminUserMixin, CreateView):
    model = Resource_info
    fields = [
        'resource_type_name'
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context

class AdminDetailView(DetailView):
    model = Resource_info
    template_name="base_app/resource_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context
    
class AdminDeleteView(AdminUserMixin, UserPassesTestMixin, DeleteView):
    model = Resource_info
    success_url = '/land-admin/listview'
    template_name = "base_app/resource_info_confirm_delete.html"

    def test_func(self):
        if self.request.user.usr_type == "Admin":
            return True
        else: 
            return False 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context

class AdminUpdateView(AdminUserMixin, UserPassesTestMixin, UpdateView):
    model = Resource_info
    fields = [
        'resource_type_name'
    ]
    success_url = '/land-admin/listview'
    
    def test_func(self):
        if self.request.user.usr_type == "Admin":
            return True
        else: 
            return False 
        
    
class MyCategoryView(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'base_app/category_view.html'
    context_object_name = 'resources'

    def get_queryset(self) -> QuerySet[Any]:
        category = self.kwargs.get('category')
        if category: 
            return self.model.objects.filter(resource_type=category)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        category = self.kwargs.get('category')
        desired = self.model.objects.filter(resource_type=category)
        count_of = desired.count()
        context = super().get_context_data(**kwargs)
        context['category'] = Resource_info.objects.get(id=category).resource_type_name
        context['status'] = Resource.objects.get(id=category).booking_status
        context['count_of'] = count_of
        context['username'] = self.request.user.username
        return context



def book_resource(request, resource_id):
  if request.method == 'POST':
    resource = Resource.objects.get(pk=resource_id)
    # Check if resource is available (implement your logic here)
    if resource.is_available():  # Replace with your availability check method
      booking = Booking.objects.create(
          resource=resource,
          booked_by=request.user,  # Access the logged-in user
          available_date=resource.get_available_date(),  # Replace with your logic to get available date
          booking_date=datetime.date.today(),  # Today's date
          current_status=0,  # Assuming booked status
      )
      booking.save()
      # Redirect with success message
      return redirect('book-resource', messages=['Resource booked successfully!'])
    else:
      # Redirect with error message
      return redirect('book-resource', messages=['Resource is not available'])
  else:
    return redirect('book-resource')  # Redirect for non-POST requests
 