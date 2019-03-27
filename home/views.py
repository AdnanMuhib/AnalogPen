from django.shortcuts import render
from os import path
import sys
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

sys.path.append('/home/hina/Music/Django/handwriting-synthesis')
import demo

count = 0

def home(request):
    return render(request, 'home/home.html')


def doc_text2(request):
    # text = request.POST.get('fileupload')
    print("Converting text to handwriting...")
    demo.generateDoc()

    return render(request, 'home/textdocument.html')


def doc_text(request):

    return render(request, 'home/textdocument.html')


@csrf_protect
@ensure_csrf_cookie
def live_text(request):
    text = request.POST.get('textarea', '')
    print(text)
    if not text == '':
        demo.generate(text)

    return render(request, 'home/livetext.html')
