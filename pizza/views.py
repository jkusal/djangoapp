from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def pizza(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        cena = request.POST.get('cena', '')
        if len(nazwa.strip()) and len(cena.strip()):
            p = Pizza(nazwa=nazwa, cena=cena)
            p.save()
            messages.success(request, "Dodano!")
        else:
            messages.error(request, "Niepoprawne dane!")

    pizza = Pizza.objects.all()
    kontekst = {'pizza': pizza}
    return render(request, 'pizza/pizza.html', kontekst)


def index(request):
    # return HttpResponse("<h1>Witaj w aplikacji Pizza!</h1>")
    return render(request, 'pizza/index.html')

def komunikat(request):
    # return HttpResponse("<h1>Witaj!</h1>")
    return render(request, 'pizza/komunikat.html')

def zamowienie(request):
    return HttpResponse("<h1>Proszę o złożenie zamówienia</h1>")

