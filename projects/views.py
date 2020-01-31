from django.shortcuts import render
from django.http import HttpResponse

from .models import Projeto 

# Create your views here.

def index(request):
    return render(request, 'projects/index.html')

def projects(request):
    projeto = Projeto.objects.get(id=1)
    return render(request, 'projects/projects.html', {"projeto": projeto})
