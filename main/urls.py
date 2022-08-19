from django.contrib import admin
from django.urls import path
from .views import index, motion, stills, music, about, data_dev

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('stills', stills, name='stills'),
    path('motion', motion, name='motion'),
    path('music', music, name='music'),
    path('about', about, name='about'),
    path('data-dev', data_dev, name='data_dev')
]