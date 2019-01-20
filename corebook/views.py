from django.shortcuts import render
from .models import Project

# Create your views here.


def mainView(request):
    projects = Project.objects.all
    return render(request, 'mainpage.html', {'projects': projects})

