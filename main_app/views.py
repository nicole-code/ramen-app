from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Ramen, Ingredient

# Define the home view
def home(request):
    return render(request, 'home.html')

def community_home(request):
    ramens =Ramen.objects.all()
    return render(request, 'community/communityhome.html', {'ramens':ramens})

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
    all_ramen_ingredients = ramen.ingredient.all()
    return render(request, 'user/userdetail.html', {'ramen': ramen, 'all_ramen_ingredients': all_ramen_ingredients})  

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
    ingredients = Ingredient.objects.all()
    return render(request, 'buildramen/new.html', {'ingredients': ingredients}) 


def buildramen_create(request):
    print('LOOK OVER HERE', request.POST)
    ramen = Ramen.objects.create(
        name=request.POST['name'],
        brand=request.POST['brand'],
        user=request.user,
    )
    if 'Chicken' in request.POST:
        ingredient_id = request.POST['Chicken']
        print("HEY I AM THE VALUE OF chicken KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id)    
    if 'Egg' in request.POST:
        ingredient_id = request.POST['Egg']
        print("HEY I AM THE VALUE OF egg KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id) 
    if 'Green Onion' in request.POST:  
        ingredient_id = request.POST['Green Onion']
        print("HEY I AM THE VALUE OF green onion KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id) 
    if 'Nori' in request.POST:  
        ingredient_id = request.POST['Nori']
        print("HEY I AM THE VALUE OF nori KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id) 
    if 'Pork Belly' in request.POST:  
        ingredient_id = request.POST['Pork Belly']
        print("HEY I AM THE VALUE OF pork belly KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id)     
    if 'Corn' in request.POST:  
        ingredient_id = request.POST['Corn']
        print("HEY I AM THE VALUE OF corn KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id) 
    if 'Naruto' in request.POST:  
        ingredient_id = request.POST['Naruto']
        print("HEY I AM THE VALUE OF naruto KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id)  
    if 'Mushroom' in request.POST:  
        ingredient_id = request.POST['Mushroom']
        print("HEY I AM THE VALUE OF mushroom KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id) 
    if 'Bean Sprouts' in request.POST:  
        ingredient_id = request.POST['Bean Sprouts']
        print("HEY I AM THE VALUE OF bean sprouts KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id)  
    if 'Tofu' in request.POST:  
        ingredient_id = request.POST['Tofu']
        print("HEY I AM THE VALUE OF tofu KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id)
    if 'Pepper' in request.POST:  
        ingredient_id = request.POST['Pepper']
        print("HEY I AM THE VALUE OF pepper KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id)
    if 'Fish Ball' in request.POST:
        ingredient_id = request.POST['Fish Ball']
        print("HEY I AM THE VALUE OF fish ball KEY", ingredient_id)
        ramen.ingredient.add(ingredient_id)                          
    
    return redirect(f'/userprofile/{ramen.id}')



def ramendetail(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.ingredient.all(ingredient_id)
    return render(request, 'buildramen/ramendetail.html', {'ramen': ramen})

def ramen_delete(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.delete()
    return redirect('home')

def user_ramen_delete(request, ramen_id):
    ramen = Ramen.objects.get(id=ramen_id)
    ramen.delete()
    return redirect('user')

