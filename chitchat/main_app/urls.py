from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chitchat/', views.chitchat_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
]