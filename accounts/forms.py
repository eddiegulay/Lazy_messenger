from django.forms import Form 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class NewUserForm(UserCreationForm):
    username = forms.CharField(label = '',widget = forms.TextInput(attrs={'class':'lazy_input m_5', 'placeholder': 'username'}))
    password1 = forms.CharField(label = '',widget = forms.PasswordInput(attrs={'class':'lazy_input m_5', 'placeholder': 'password'}))
    password2 = forms.CharField(label = '',widget = forms.PasswordInput(attrs={'class':'lazy_input m_5', 'placeholder': 'confirm password'}))

class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(label = 'profile image', widget= forms.FileInput(attrs = None))
    class Meta:
        model = Profile
        fields = ['profile_image']
        
        
