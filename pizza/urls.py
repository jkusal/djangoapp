from django.conf.urls import path

from . import views

urlspatterns = [
    path('', views.index, name='index'),
]