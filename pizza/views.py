from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("<h1>Witaj w aplikacji Pizza!</h1>")
    return render(request, 'pizza/index.html')

def komunikat(request):
    # return HttpResponse("<h1>Witaj!</h1>")
    return render(request, 'pizza/komunikat.html')

def zamowienie(request):
    return HttpResponse("<h1>Proszę o złożenie zamówienia</h1>")
