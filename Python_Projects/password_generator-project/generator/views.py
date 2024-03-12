from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {"password": 'asdkf'})


def eggs(request):
    return HttpResponse('<h1>Eggs are great</h1>')
