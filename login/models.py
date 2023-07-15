from django.db import models
from django.contrib.auth.models import User


# This model will be for a new user to sign up
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')  # images will be uploaded to profile_pics folder


