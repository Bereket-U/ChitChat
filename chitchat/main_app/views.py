from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrForm

# Create your views here.
def home(request):
    return render (request, 'home.html')

def chitchat_index(request):
    return render(request, 'chitchat/index.html')

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