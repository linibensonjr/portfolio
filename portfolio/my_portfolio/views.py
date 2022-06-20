from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def port(request):
    return render(request, 'my_portfolio/index.html')


def skills(request):
    return render(request, 'my_porfolio/skills.html')
