from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Witaj w aplikacji Pizza!</h1>")

def komunikat(request):
    return HttpResponse("<h1>Witaj!</h1>")

def zamowienie(request):
    return HttpResponse("<h1>Proszę o złożenie zamówienia</h1>")
