from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Ramen, Ingredient

# Define the home view
def home(request):
    ramens =Ramen.objects.all()
    return render(request, 'home.html', {'ramens':ramens})

def communitydetail(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    return render(request, 'community/communitydetail.html', {'ramen': ramen})    

def login_user(request):
    return render(request, 'registration/login.html')

def user_profile(request):
    ramens = Ramen.objects.filter(user=request.user)
    return render(request, 'user/userprofile.html', { 'ramens': ramens })

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


#view to show the build form
def buildramen_new(request):
    return render(request, 'buildramen/new.html') 

#view to handle incoming form data

def buildramen_create(request):
    print(request.POST)
    ramen = Ramen.objects.create(
        name=request.POST['name'],
        brand=request.POST['brand'],
        # ingredient=request.POST['ingredient'],
        user=request.user,
    )
    print(ramen)
    return redirect(f'/buildramen/{ramen.id}')

def ramendetail(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    return render(request, 'buildramen/ramendetail.html', {'ramen': ramen})

def ramen_delete(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.delete()
    return redirect('home')

def user_ramen_delete(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.delete()
    return redirect('user')

