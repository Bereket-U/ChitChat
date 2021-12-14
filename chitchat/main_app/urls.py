from django.urls import path
from . import views
from django.views.generic.edit import CreateView

urlpatterns = [

  path('', views.landing, name='landing'),
  path('signup/', views.signup, name='signup'),
  path('home/', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('edit-post/', views.edit_post, name='edit_post'),
  path('post-confirm-delete/', views.post_confirm_delete, name='post_confirm_delete'),
  path('comment-confirm-delete/', views.comment_confirm_delete, name='comment_confirm_delete'),
  path('chitchat/', views.chitchat_index, name='index'),
  path('accounts/signup/', views.signup, name='signup'),
  path('post/<int:post_id>/', views.post, name='post'),
  path('post/create/', views.PostCreate.as_view(), name='post_create'),
  path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
  path('post/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
]
