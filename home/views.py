from django.shortcuts import render
from os import path
import sys
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

sys.path.append('/home/hina/Music/Django/handwriting-synthesis')
import demo


def home(request):
    return render(request, 'home/home.html')


@csrf_protect
@ensure_csrf_cookie
def live_text(request):
    text = request.POST.get('textarea', '')
    print(text)
    if not text == '':
        demo.generate(text)

    return render(request, 'home/livetext.html')


def generate_text(request):
    text = request.POST.get('textarea')
    print(text)
    # demo.generate(text)
    return render(request, 'home/livetext.html')
