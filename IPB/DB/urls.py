from django.contrib import admin
from django.urls import path, include
from DB import views


urlpatterns = [
    path('generate', views.generate, name='generate'),
    path('regenerate', views.regenerate, name='regenerate'),
    path('practise', views.practise, name='practise'),
    # path('submit', views.submit, name='submit'),
    path('upload', views.upload_audio, name='upload_audio'),
]
