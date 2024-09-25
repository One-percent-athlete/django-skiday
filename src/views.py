from django.shortcuts import render
import datetime

def home(request):
    year = datetime.datetime.now().year
    return render(request, 'pages/home.html', {"year":year})

def info(request):
    year = datetime.datetime.now().year
    return render(request, 'pages/info.html', {"year":year})