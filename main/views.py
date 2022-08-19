from django.shortcuts import render
# from django.views import View

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stills(request):
    return render(request, 'stills.html')

def motion(request):
    return render(request, 'motion.html')

def music(request):
    return render(request, 'music.html')

def about(request):
    return render(request, 'about.html')

def data_dev(request):
    return render(request, 'data-dev.html')