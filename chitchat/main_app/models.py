from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=250)
    created_at = models.DateTimeField(default= datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.id})
    

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(default= datetime.datetime.now())
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
      
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.post.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"


class ProfilePicture(models.Model):
    url = models.CharField(max_length=200)
    bio = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"user_id: {self.user_id} @{self.url}"