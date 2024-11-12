from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def catalogue(request):
    return HttpResponse("It is Catalogue page!")

def index(request):
    return HttpResponse("It is Index page!")

def notFound(request):
    return HttpResponse("<h1>Not F O U N D</h1><p>404!</p>")