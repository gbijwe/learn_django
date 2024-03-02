from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse
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
            if user_type == "Company":
                return redirect('land-company')
            else: 
                return redirect('land-admin')
    else:
        form = UserRegisterForm()
    return render(request, 'base_app/register.html', {'form': form})

@login_required
def myAdmin(request):
    context = {
        "title" : request.user.username,
    }
    return render(request, 'base_app/home.html', context)

@login_required
def myCompany(request):
    context = {
        "title" : request.user.username,
    }
    return render(request, 'base_app/home.html', context)

def landing_page(request):
    # return HttpResponse("<h3>Welcome to the Bench App.</h3>")
    return render(request, 'base_app/landing.html')

class MyLoginView(LoginView):
    redirect_authenticated_user = False
    
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