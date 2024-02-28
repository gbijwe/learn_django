from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

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
            if user_type == "Admin":
                return redirect('company-page')
            else: 
                return HttpResponse("Not an admin")
    else:
        form = UserRegisterForm()
    return render(request, 'base_app/register.html', {'form': form})

def myAdmin(request):
    return HttpResponse("<h1>welcome admin</h1>")
def myCompany(request):
    return HttpResponse("<h1>welcome company</h1>")