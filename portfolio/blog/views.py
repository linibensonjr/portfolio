import imp
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from django.utils import timezone

# Create your views here.
def blog(request):
    blogpost = Blog.objects.filter(date_pub__lte=timezone.now()).order_by('-date_pub')
    context = {blogpost:'blogpost'}
    return render(request, 'blog/blog.html', context)