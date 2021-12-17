from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from .forms import UserRegistrForm, CommentForm, PostForm, UserUpdateForm, UpdateComment, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Photo, ProfilePicture
from django.views.generic import CreateView, UpdateView, DeleteView
import uuid
import boto3
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin



S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'chitchat'

# Create your views here.
@login_required
def add_photo(request, post_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            if Photo.objects.filter(post_id = post_id).exists():
              p = Photo.objects.get(post_id = post_id)
              p.url = url
              p.save()
            else: 
              photo = Photo(url=url, post_id=post_id)
              photo.save()
        except Exception as e:
            print(e)
    return redirect('post', post_id=post_id)

@login_required
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
  
# class PostUpdate(UpdateView):
#   model = Post
#   fields = ['text']

@login_required
def post_update(request, pk):
  error_message = ''
  print(pk)
  
  if request.method == 'POST':
    p = Post.objects.get(id = pk)
    print(request.POST['text'])
    p.text = request.POST['text']
    p.save()
    add_photo(request, pk)
    return redirect('post', post_id = pk)
  else:
    error_message = 'Invalid Inputs'
  post_form = PostForm()
  context= {"post_form": post_form, 'post_id' : pk, 'error_message': error_message}
  return render(request, 'main_app/update_post_form.html', context)


class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/profile/'

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = UpdateComment
 
@login_required
def chitchat_index(request):
    return render(request, 'chitchat/index.html')

@login_required
def landing(request):
  return redirect('login')

@login_required
def home(request):
  posts = Post.objects.all()
  profile = ProfilePicture.objects.get(user_id=request.user)
  print(profile)
  return render(request, 'home.html', {'posts': posts, 'profile' : profile})

@login_required
def post(request, post_id):
  post = Post.objects.get(id=post_id)
  comment_form = CommentForm()
  return render(request, 'posts/detail.html', { 'post': post, 'comment_form': comment_form })

@login_required
def add_comment(request, post_id, user_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.user_id = user_id
    new_comment.save()
  return redirect('post', post_id=post_id)

@login_required
def profile(request):
    posts = Post.objects.filter(user=request.user)
    profile = ProfilePicture.objects.get(user_id=request.user)
    
    return render(request, 'profile.html', {'posts': posts, 'profile': profile})

@login_required
def edit_post(request):
  return render(request, 'posts/edit_post.html')

@login_required
def post_confirm_delete(request):
  return render(request, 'posts/post_confirm_delete.html')

@login_required
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
    # except ProfilePicture.DoesNotExist:
    #     return None
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def CommentDelete(request, comment_id, post_id):
    Comment.objects.filter(id=comment_id).delete()
    return redirect('post', post_id=post_id)

@login_required
def add_profile_picture(request, user_id):
    profile_form = ProfileForm(request.POST)
    print('profile form', profile_form)
    if profile_form.is_valid():
       profile_form.instance.user_id = request.user.id
       profile = profile_form.save()
       print('profile', profile)
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            if ProfilePicture.objects.filter(user_id = user_id).exists():
              # profile = ProfilePicture.objects.get(user_id = user_id)
              profile.url = url
              d = profile.save()
              print('added photo', d)
            else: 
              photo = ProfilePicture(url=url, user_id=user_id, bio = '')
              photo.save()
        except Exception as e:
            print(e)
    return redirect('edit_profile')

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'main_app/edit_user_form.html'
    success_url = '/edit_profile/'

    def get_object(self):
        return self.request.user

class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    from_class = PasswordChangeForm
    template_name = 'main_app/change_password_form.html'
    success_url = '/change_password_done/'

class PasswordsChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'main_app/change_password_done.html'

class PasswordsResetView(LoginRequiredMixin, PasswordResetView):
    from_class = PasswordResetForm
    template_name = 'main_app/reset_password_form.html'
    success_url = '/reset_password_done/'

class PasswordsResetDoneView(LoginRequiredMixin, PasswordResetDoneView):
    template_name = 'main_app/reset_password_done.html'
    success_url = '/change_password_done/'

