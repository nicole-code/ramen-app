from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class CreateUserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']