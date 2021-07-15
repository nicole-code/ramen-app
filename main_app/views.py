from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Ramen, Ingredient

# Define the home view
def about(request):
    return render(request, 'about.html')

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

def user_ramen_detail(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    return render(request, 'user/userdetail.html', {'ramen': ramen})  

def user_ramen_edit(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    return render(request, 'user/editramen.html', {'ramen': ramen}) 

def user_ramen_update(request, ramen_id):
    print('RAMEN RAMEN RAMEN RAMEN RAMEN RAMEN RAMEN')
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.name = request.POST['name']
    ramen.brand = request.POST['brand']
    # ADD INGREDIENTS UPDATE HERE
    ramen.save()
    return redirect('home') 

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


def buildramen_create(request):
    ramen = Ramen.objects.create(
        name=request.POST['name'],
        brand=request.POST['brand'],
        # ingredient=request.POST['name'],
        user=request.user,
    )
    # Ramen.objects.get(id=ramen_id).ingredient.add(ingredient_id)
    return redirect(f'/buildramen/{ramen.id}')



def ramendetail(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    # ingredient = Ingredient.objects.get(id=ingredient_id)
    # ramen.ingredient.add(ingredient)
    return render(request, 'buildramen/ramendetail.html', {'ramen': ramen})

def ramen_delete(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.delete()
    return redirect('home')

def user_ramen_delete(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.delete()
    return redirect('user')

