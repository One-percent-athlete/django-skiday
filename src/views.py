from django.shortcuts import render
import datetime

year = datetime.datetime.now().year

def home_en(request):
    return render(request, 'pages/home_en.html', {"year":year})

def home_jp(request):
    return render(request, 'pages/home_jp.html', {"year":year})

def info(request):
    
    return render(request, 'pages/info.html', {"year":year})

def mtcam(request):

    return render(request, 'pages/mtcam.html', {"year":year})

def powderalert(request):

    return render(request, 'pages/powderalert.html', {"year":year})

def matching(request):

    return render(request, 'pages/matching.html', {"year":year})

def niseko_en(request):

    return render(request, 'pages/niseko_en.html', {"year":year})

def niseko_jp(request):

    return render(request, 'pages/niseko_jp.html', {"year":year})
