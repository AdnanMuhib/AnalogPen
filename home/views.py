from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def live_text(request):
    return render(request, 'home/livetext.html')
