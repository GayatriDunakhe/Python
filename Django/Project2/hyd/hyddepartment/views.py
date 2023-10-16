from django.http import HttpResponse
from django.shortcuts import render
from .models import Infyx

def hello_world(request):
    return HttpResponse("Hello world")

def show(request):
    return render(request, 'index.html')

def name_list(request):
    names = Infyx.objects.all()
    return render(request, 'index.html', {'names': names})

def num_list(request):
    numbers= range(1,11)
    return render(request, 'index.html', {'numbers': numbers})

def agecheck(request):
    age = 64
    return render(request, 'index.html', {'age': age})