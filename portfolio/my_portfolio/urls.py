from django.urls import path
from django import urls
from . import views
# from portfolio.blog import views

urlpatterns = [
    path('', views.port, name='home'),
    path('skills/', views.skills, name='skills')
    # path('blog/', views.blog, name='blog')
]