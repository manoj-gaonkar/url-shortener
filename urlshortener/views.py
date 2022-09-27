from django.shortcuts import render, redirect
from pyshorteners import Shortener

# Create your views here.
def index(request):
    
    if request.method == "POST":
        longurl = request.POST['longurl']
        tiny = Shortener()
        shorturl = tiny.tinyurl.short(longurl)
        print(shorturl)

        context = { "shorturl": shorturl, 'valuepost': 'gnadu' }
    else:
        context = {}

    return render(request, 'index.html',context)