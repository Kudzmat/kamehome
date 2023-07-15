from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


# django has built in UserCreationForm which this class will inherit from
# This form will be for new users to sign up
class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # fields we want access to


# This form will be for when a user wants to edit their information
# Inheriting from django's UserChangeForm
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


