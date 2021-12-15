from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from .forms import UserRegistrForm, CommentForm, PostForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Photo
from django.views.generic import CreateView, UpdateView, DeleteView
import uuid
import boto3



S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'chitchat'

# Create your views here.

def add_photo(request, post_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, post_id=post_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    print('about to redirect and add photo')
    return redirect('post', post_id=post_id)

def post_create(request):
  error_message = ''

  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      post_form.instance.user_id = request.user.id
      post = post_form.save()
      add_photo(request, post.id)
      return redirect('post', post_id=post.id)

  else:
      error_message = 'Invalid Inputs'

  post_form = PostForm()
  context= {"post_form" : post_form, 'error_message': error_message}

  return render(request, 'main_app/post_form.html', context)
  
class PostUpdate(UpdateView):
  model = Post
  fields = ['text']

class PostDelete(DeleteView):
  model = Post
  success_url = '/profile/'

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['comment']
 
@login_required
def chitchat_index(request):
    return render(request, 'chitchat/index.html')

def landing(request):
  return redirect('login')

def home(request):
  posts = Post.objects.all()
  return render(request, 'home.html', {'posts': posts})


def post(request, post_id):
  post = Post.objects.get(id=post_id)
  comment_form = CommentForm()
  return render(request, 'posts/detail.html', { 'post': post, 'comment_form': comment_form })

def add_comment(request, post_id, user_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.user_id = user_id
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


def CommentDelete(request, comment_id, post_id):
    Comment.objects.filter(id=comment_id).delete()
    return redirect('post', post_id=post_id)

class UserEditView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'main_app/edit_user_form.html'
    success_url = '/edit_profile/'

    def get_object(self):
        return self.request.user
