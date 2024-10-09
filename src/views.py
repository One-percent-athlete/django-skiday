from django.shortcuts import render
from django.contrib import messages


def info(request):
    return render(request, 'info.html')

def home_en(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        company = request.POST["company"]
        message = request.POST["message"]
        return render(request, 'home_en.html', {"name": name})
    return render(request, 'home_en.html')

def mtcam(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        company = request.POST["company"]
        message = request.POST["message"]

        return render(request, 'mtcam.html' ,{"name": name})
    return render(request, 'mtcam.html')

def powderalert(request):
    return render(request, 'powderalert.html')

def matching(request):
    return render(request, 'matching.html')

def niseko_en(request):
    return render(request, 'niseko_en.html')

def niseko_jp(request):
    return render(request, 'niseko_jp.html')
