from django.shortcuts import render


def home_en(request):
    return render(request, 'home_en.html')



def info(request):
    
    return render(request, 'info.html')

def mtcam(request):

    return render(request, 'mtcam.html')

def powderalert(request):

    return render(request, 'powderalert.html')

def matching(request):

    return render(request, 'matching.html')

def niseko_en(request):

    return render(request, 'niseko_en.html')

def niseko_jp(request):

    return render(request, 'niseko_jp.html')
