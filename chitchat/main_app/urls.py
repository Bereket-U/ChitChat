from django.contrib import auth
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
  path('post/create/', views.post_create, name='post_create'),
  path('post/<int:post_id>/add_comment/<int:user_id>', views.add_comment, name='add_comment'),
  path('comment/<int:comment_id>/delete/<int:post_id>', views.CommentDelete, name='comment_delete'),
  path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
  path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
  path('post/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
  path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
  path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
  path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
  path('change_password/', views.PasswordsChangeView.as_view(), name='change_password'),
  path('change_password_done/', views.PasswordsChangeDoneView.as_view(), name='change_password_done'),
  path('reset_password/', views.PasswordsResetView.as_view(), name='reset_password'),
  path('reset_password_done/', views.PasswordsResetDoneView.as_view(), name='reset_password_done'),
  
]