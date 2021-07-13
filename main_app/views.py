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

def edit_profile(request):
    return render(request, 'usereditprofile.html')

# def user_update_form(request, profile_id):
#     print("update form")
#     profile = Profile.objects.get(id=profile_id)
#     profile.user = request.POST['user']
#     profile.email = request.POST['email']
#     profile.save()
#     print("hello")
#     return redirect(f'/userprofile/{profile.id}')

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


<<<<<<< HEAD

=======
def buildramen(request):
    return render(request, 'buildramen.html') 
>>>>>>> main

