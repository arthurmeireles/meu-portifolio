from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'projects/index.html')

def projects(request):
    return render(request, 'projects/projects.html')