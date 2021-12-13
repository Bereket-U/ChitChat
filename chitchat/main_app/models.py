from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=250)
    created_at = models.DateTimeField(default= datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(default= datetime.datetime.now())

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
