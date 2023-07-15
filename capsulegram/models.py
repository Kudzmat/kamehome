from django.db import models
from django.contrib.auth.models import User


# For users to upload to the capsule gram
class CapsuleGram(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    image = models.ImageField(upload_to='capsule_gram', blank=False)
    caption = models.TextField(default='DragonBall Moment')
    upload_date = models.DateTimeField(auto_now_add=True)  # automatically adds date when image is uploaded

    def __str__(self):
        return self.caption


# a comment must be related to a user and a gram post
class Comments(models.Model):
    gram_post = models.ForeignKey(CapsuleGram, on_delete=models.CASCADE, related_name="post_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']  # latest comment will be at the top

    def __str__(self):
        return self.comment


# A like will be linked to a user and a blog post
class Likes(models.Model):
    gram_post = models.ForeignKey(CapsuleGram, on_delete=models.CASCADE, related_name="liked_pic")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
