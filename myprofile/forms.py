from django import forms
from login.models import UserProfile


# This form will be for updating a profile picture
class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']


