from django.shortcuts import render

# Create your views here.

def login(request):
  return render(request, 'login.html')


def signup(request):
  return render(request, 'signup.html')


def home(request):
  return render(request, 'home.html')


def post(request):
  return render(request, 'posts/detail.html')


def profile(request):
  return render(request, 'profile.html')


def edit_post(request):
  return render(request, 'edit_post.html')


def post_confirm_delete(request):
  return render(request, 'post_confirm_delete.html')


def comment_confirm_delete(request):
  return render(request, 'comment_confirm_delete.html')

