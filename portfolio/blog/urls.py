from django.urls import path
from django import urls
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
]