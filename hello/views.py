from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index1(request):
    return HttpResponse("Hello, world!")

def index(request):
    return render(request, "hello/index.html")

def uaa490(request):
    return HttpResponse("Hello, class!")

def josh(request):
    return HttpResponse("Hello, josh!")

def greet1(request, name):
    return HttpResponse(f"<h1>Greetings, {name}!</h1><p>What's happening?</p>")

def greet(request, name):
    return render(request, "hello/greet.html", {"greetee": name.capitalize()})
