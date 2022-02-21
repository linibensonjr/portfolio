import imp
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from django.utils import timezone

# Create your views here.
def blog(request):
    blogpost = Blog.objects.all()
    context = {'blogpost':blogpost}
    return render(request, 'blog/blog.html', context)