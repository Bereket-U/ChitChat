from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import CreateView
from .forms import CommentForm


# Create your views here.

class PostCreate(CreateView):
  model = Post
  fields = ['text']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

    
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
  comment_form = CommentForm()
  return render(request, 'posts/detail.html', { 'post': post, 'comment_form': comment_form })

def add_comment(request, post_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.save()
  return redirect('post', post_id=post_id)

def profile(request):
    posts = Post.objects.filter(user=request.user)
    
    return render(request, 'profile.html', {'posts': posts})


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