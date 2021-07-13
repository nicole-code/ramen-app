from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

BRANDS = (
    (),
    (), 
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
)

class Ramen(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    #     choices = BRANDS,
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)

    