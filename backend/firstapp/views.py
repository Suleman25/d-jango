from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Triggered</h1>')
def jan(request):
    return HttpResponse('<h1>learn python</h1>')
def feb(request):
    return HttpResponse('<i>learn DJANGo</i>')