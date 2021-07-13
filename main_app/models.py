from django.db import models
from django.contrib.auth.models import User

class Ramen(models.Model):
    brand = models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)
    spice = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

    