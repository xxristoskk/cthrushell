from django.shortcuts import render
# from django.views import View

# Create your views here.
def index(request):
    return render(request, 'index.html')

def glitch_art(request):
    return render(request, 'glitch-art.html')

def ai_art(request):
    return render(request, 'ai-art.html')

def music(request):
    return render(request, 'music.html')

def about(request):
    return render(request, 'about.html')

def data_dev(request):
    return render(request, 'data-dev.html')