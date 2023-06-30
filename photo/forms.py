from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import *

class CustomUserCreationForm(UserCreationForm):
     class Meta:
          model = User
          fields = [
               'username', 'password1', 'password1'
          ]
          labels = {
               'username':'Username',
               'password1':'Password',
               'password2':'Confirm Password'
          }

class CategoryForm(forms.ModelForm):
     class Meta:
          model = Category
          fields ="__all__"
          labels = {
               'user':'Username',
               'name':'Category Name'
          }

class PhotoForm(forms.ModelForm):
     class Meta:
          model = Photo
          fields ="__all__"
          labels = {
               'category':'Category Name',
               'title':'Title',
               'image':'Image'
          }
     
      