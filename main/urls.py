from django.contrib import admin
from django.urls import path
from .views import index, ai_art, animation, music, about, stills

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('ai_art/', ai_art, name='ai_art'),
    path('animation/', animation, name='animation'),
    path('music/', music, name='music'),
    path('/about', about, name='about'),
    path('/stills', stills, name='stills')
]