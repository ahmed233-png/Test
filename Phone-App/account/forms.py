from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NewUserRegister(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'maxlength':'8'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'maxlength':'8'}))
  
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
