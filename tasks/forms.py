# forms.py
from django import forms 
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 

from django.forms.widgets import PasswordInput  ,TextInput

class POSTform (forms.ModelForm):
    class Meta:
        model= Task
        fields=['title','description','completed']
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput)

    
