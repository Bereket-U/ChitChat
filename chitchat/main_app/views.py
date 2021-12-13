from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrForm
from django.contrib.auth.decorators import login_required

# Create your views here.
    
@login_required
def chitchat_index(request):
    return render(request, 'chitchat/index.html')


def login(request):
  return render(request, 'login.html')


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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserRegistrForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserRegistrForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
