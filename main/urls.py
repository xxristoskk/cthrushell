from django.contrib import admin
from django.urls import path
from .views import index, ai_art, glitch_art, music, about, data_dev

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('glitch-art', glitch_art, name='glitch_art'),
    path('ai-art', ai_art, name='ai_art'),
    path('music', music, name='music'),
    path('about', about, name='about'),
    path('data-dev', data_dev, name='data_dev')
]