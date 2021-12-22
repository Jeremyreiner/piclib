from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ['full_name','phone', 'bio','profile_image']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields= ['full_name','first_name','last_name', 'phone', 'bio','profile_image']