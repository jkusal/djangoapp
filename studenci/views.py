from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from studenci.models import Miasto, Uczelnia
from studenci.forms import UserLoginForm, UczelniaForm, MiastoForm
# Create your views here.

def index(request):
    return HttpResponse("<h1>Witaj w aplikacji Studenci!</h1>")
    # return render(request, 'studenci/index.html')

def miasta(request):
    if request.method == 'POST':
        # nazwa = request.POST.get('nazwa', '')
        # kod = request.POST.get('kod', '')
        # if len(nazwa.strip()) and len(kod.strip()):
        form = MiastoForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "Dodano!")
            return redirect(reverse('studenci:miasta'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = MiastoForm

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta, 'form': form}
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):
    if request.method == 'POST':
       # nazwa = request.POST.get('nazwa', '')
        # if len(nazwa.strip()):
        form = UczelniaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Dodano!")
            return redirect(reverse('studenci:uczelnie'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = UczelniaForm

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie, 'form': form}
    return render(request, 'studenci/uczelnie.html', kontekst)

def loguj_studenta(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'studenci/login.html', kontekst)