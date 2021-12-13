from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrForm
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
    
@login_required
def chitchat_index(request):
    return render(request, 'chitchat/index.html')

def landing(request):
  return redirect('login')

def login(request):
  return render(request, 'registration/login.html')


def home(request):
  posts = Post.objects.all()
  return render(request, 'home.html', {'posts': posts})


def post(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', { 'post': post })


def profile(request):
  return render(request, 'profile.html')


def edit_post(request):
  return render(request, 'posts/edit_post.html')


def post_confirm_delete(request):
  return render(request, 'posts/post_confirm_delete.html')


def comment_confirm_delete(request):
  return render(request, 'posts/comment_confirm_delete.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserRegistrForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserRegistrForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
