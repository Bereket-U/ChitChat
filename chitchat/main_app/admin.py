from django.contrib import admin
from .models import Post, Comment, ProfilePicture

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ProfilePicture)