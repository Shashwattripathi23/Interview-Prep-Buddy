from django.contrib import admin
from django.urls import path, include
from DB import views


urlpatterns = [
    path('generate', views.generate, name='generate'),
]
