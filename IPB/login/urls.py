from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log', views.log, name='log'),
    path('signup', views.signup, name='signup'),
    path('login', views.loginn, name='login'),

]
