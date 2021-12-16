from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, widgets
from .models import Comment, Post, ProfilePicture


class UserRegistrForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']

class UpdateComment(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['text']


class UserUpdateForm(ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(ModelForm):
  class Meta:
    model = ProfilePicture
    fields = ['bio']