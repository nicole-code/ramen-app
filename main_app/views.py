from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Ramen
from .models import Ingredient
from .models import Profile

# Define the home view
def home(request):
    ramens =Ramen.objects.all()
    return render(request, 'home.html', {'ramens':ramens})

def loginuser(request):
    return render(request, 'registration/login.html')

def userprofile(request):
    return render(request, 'userprofile.html')    

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

