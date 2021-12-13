from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=250)
    created_at = models.DateTimeField(default= datetime.datetime.now())