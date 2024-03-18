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

from .models import Resource, Resource_info, Booking, CustomUsers
import datetime
from django.contrib.auth.decorators import login_required
from .admin import BookingResource
from django.db.models import Count, Sum


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

class CategoryListView(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'base_app/category_list.html'
    context_object_name = 'resources'
    ordering = ['resource_type']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username
        return context
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

class MyListView(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'base_app/resource_list.html'
    context_object_name = 'resources'
    ordering = ['resource_type']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Add a flag 'is_available' to each resource
        for resource in queryset:
            resource.is_available = resource.available_date <= datetime.date.today()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username

        return context


class MyDetailView(LoginRequiredMixin, DetailView):
    model = Resource
    template_name="base_app/resource_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usr_type'] = self.request.user.usr_type
        context['username'] = self.request.user.username

        resource = self.get_object()
        # Check if the logged-in user is the creator of the resource
        if self.request.user == resource.created_by:
            context['is_creator'] = True
        else:
            context['is_creator'] = False
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
         'resource_name', 'resource_type', 'description', 'available_date'
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

class AdminDetailView(AdminUserMixin, DetailView):
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
        context['usr_type'] = self.request.user.usr_type
        return context


@login_required
def book_resource(request, resource_id):
  if request.method == 'POST':
    resource = Resource.objects.get(pk=resource_id)
    booking_date=datetime.date.today()
    # Check if resource is available (implement your logic here)
    if resource.booking_status == 1 and resource.available_date <= booking_date:  # Replace with your availability check method
      booking = Booking.objects.create(
          resource=resource,
        #   res_id = resource.id,
          res_type = str(resource.resource_type),
          booked_by=request.user,  # Access the logged-in user
          available_date=resource.available_date,  # Replace with your logic to get available date
          booking_date=booking_date,  # Today's date
          current_status=1,
        #   owner = str(resource.created_by),
          owner = resource.created_by.get_username(),  
      )
      print(resource.created_by)
      booking.save()
      resource.booking_status = 0
      resource.save()
    #   return redirect('bookresource', messages=['Resource booked successfully!'])
      return redirect('booking-view')
    else:
      # Redirect with error message - resource is already booked

      return redirect('land-company')
    #   return redirect('listview', messages=['Resource is not available'])
  else:
    # return redirect('listview')  # Redirect for non-POST requests
    return HttpResponse("Method is not POST.")


@login_required
def release_resource(request, my_id):
    if request.method == 'POST':
        resource = Resource.objects.get(id=my_id)
        stat = Booking.objects.filter(resource_id=my_id).order_by('-created_at').first()
        # print(Booking.models.objects.current_status)
        if resource.booking_status == 0:  # Assuming 0 indicates the resource is booked
            resource.booking_status = 1  # Marking the resource as available
            resource.release_date = datetime.date.today().isoformat()
            resource.available_date = datetime.date.today().isoformat()  # Setting release date as today's date
            resource.save()
            messages.success(request, 'Resource released successfully!')
            
            stat.current_status = 0
            stat.release_date = datetime.date.today().isoformat()
            stat.available_date = datetime.date.today().isoformat()
            stat.save()
            return redirect('booking-view')

        else:
            messages.error(request, 'Resource is already available.')
            return redirect('booking-view')
    else:
        return HttpResponse("Method is not POST.")



# View my bookings and download them in XLS file.

class BookingView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'base_app/my_bookings.html'
    context_object_name = 'resources'
    ordering=['-current_status']

    def get_queryset(self):
        qs = super().get_queryset().filter(booked_by=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['usr_type'] = self.request.user.usr_type
        return context

    def post(self, request):
        qs = self.get_queryset().filter(booked_by=self.request.user)
        dataset = BookingResource().export(qs)
        ds = dataset.xls

        response = HttpResponse(ds, content_type='xls')
        response['Content-Disposition'] = f"attachment; filename=posts.xls"
        return response

class MyResources(LoginRequiredMixin, ListView):
    model = Resource
    template_name='base_app/my_list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        qs = super().get_queryset().filter(created_by=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['usr_type'] = self.request.user.usr_type
        return context

@login_required
def statistics_view(request):
    current_user = request.user

    total_resources = Resource.objects.count
    my_total_resources = Resource.objects.filter(created_by=current_user).count
    booked_till_date = Booking.objects.filter(booked_by=current_user).count
    current_booked = Booking.objects.filter(booked_by=current_user, current_status=True).count
    total_users = CustomUsers.objects.filter(usr_type="Company").count

    context = {
        'my_total_resources' : my_total_resources,
        'total_resources' : total_resources,
        'booked_till_date' : booked_till_date, 
        'current_booked' : current_booked,
        'usr_type' : current_user.usr_type,
        'username' : current_user.username,
        'total_users': total_users,
    }

    return render(request, 'base_app/home.html', context)