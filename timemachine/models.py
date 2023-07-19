from django.db import models
from login.models import UserProfile
from django.contrib.auth.models import User


# when users time travel they will get a story description and two images to go along with it
class TimelineStory(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_author')
    description = models.TextField(max_length=3000, blank=False)
    dragon_title = models.TextField(max_length=100)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.dragon_title
