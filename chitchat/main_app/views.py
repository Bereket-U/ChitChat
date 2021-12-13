from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html')

def chitchat_index(request):
    return render(request, 'chitchat/index.html')