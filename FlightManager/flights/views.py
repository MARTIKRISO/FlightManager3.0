from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from . import models

def index(request):
    return render(request, "flights/index.html")

def book(request, pk):
    flight = get_object_or_404(models.Flight, pk = pk)
    ctx = {
        "data": flight
    }
    return render(request, "flights/book.html", ctx)

def seeflights(request):
    data = get_list_or_404(models.Flight)
    print(data)
    ctx = {
        "data": data
    }
    return render(request, "flights/seeflights.html", ctx)

def login(request):
    return render(request, "flights/login.html")