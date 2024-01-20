from django.contrib import admin
from django.urls import path, include
from DB import views


urlpatterns = [
    path('<str:name>/generate', views.generate, name='generate'),
    path('<str:name>/regenerate', views.regenerate, name='regenerate'),
    path('<str:name>/practise', views.practise, name='practise'),
    # path('submit', views.submit, name='submit'),
    # path('upload', views.upload_audio, name='upload_audio'),
    path('<str:name>/start', views.start, name='start'),
    path('<str:name>/end',  views.end, name='end'),
]
