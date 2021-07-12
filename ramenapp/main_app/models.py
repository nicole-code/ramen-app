from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Ramen(models.Model):
    brand = models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)
    spice = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)



    