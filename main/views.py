from django.shortcuts import render
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ai_art(request):
    return render(request, 'ai-art.html')

def animation(request):
    return render(request, 'animation.html')

def music(request):
    return render(request, 'music.html')

def about(request):
    return render(request, 'about.html')

def stills(request):
    return render(request, 'stills.html')