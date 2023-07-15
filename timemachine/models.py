from django.db import models


# when users time travel they will get a story description and two images to go along with it
class TimelineStory(models.Model):
    description = models.TextField(max_length=2500, blank=False)
    dragon_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)  # automatically adds date when post is published
    image1 = models.ImageField(upload_to='travel_pics', blank=False)
    image2 = models.ImageField(upload_to='travel_pics', blank=False)

    def __str__(self):
        return self.dragon_title
