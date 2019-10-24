from django.shortcuts import render
from django.http import HttpResponse
from studenci.models import Miasto, Uczelnia
# Create your views here.

def index(request):
    return HttpResponse("<h1>Witaj w aplikacji Studenci!</h1>")
    # return render(request, 'studenci/index.html')

def miasta(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        kod = request.POST.get('kod', '')
        m = Miasto(nazwa=nazwa, kod=kod)
        m.save()

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta}
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        u = Uczelnia(nazwa=nazwa)
        u.save()

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie}
    return render(request, 'studenci/uczelnie.html', kontekst)