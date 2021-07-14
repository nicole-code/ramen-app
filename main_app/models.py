from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


class Ramen(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    #     choices = BRANDS,
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ingredient = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.name

