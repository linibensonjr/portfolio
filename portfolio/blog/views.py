from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return HttpResponse('<h2>This is a blog page</h2>')