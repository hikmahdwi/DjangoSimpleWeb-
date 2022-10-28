from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def hikmah(request):
    return HttpResponse("Hello, Hikmah Dwiyanti Nasir!")

def dear(request):
    return HttpResponse("Hello, Dear No One!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })