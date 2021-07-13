from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

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
    brand = models.CharField(max_length=100)(
        choices = BRANDS,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Ingredient = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.name


    