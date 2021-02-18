from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from . import models

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


#editing user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ] 

class  ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            
            'phone',
        ]               