from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from . import models
import json
from argon2 import PasswordHasher #Most secure hashing algo

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
    if request.method == "GET":
        return render(request, "flights/login.html")
    else:
        data = json.loads(request.POST.get("order"))

        username = data.get("username")
        password = data.get("password")
        #TODO: Handle hashing and logging in

        dbrecord = get_object_or_404(models.User, username=username)

        print(dbrecord)

        return HttpResponse("OK")


def checkout(request):
    return render(request, "flights/checkout.html")

def flightdata(request):
    pk = request.GET.get("pk", None)
    flight = get_object_or_404(models.Flight, pk= pk)
    return HttpResponse(serializers.serialize("json", [flight, ]))

def reserve(request):
   
    data = json.loads(request.POST.get("order"))

    flight = get_object_or_404(models.Flight, pk=data[0].get("flight"))

    for item in data:        
        res_object = models.Reservation(
            f_name= item.get("f_name"),
            m_name= item.get("m_name"),
            l_name= item.get("l_name"),
            EGN= item.get("EGN"),
            email= item.get("email"),
            phone_number= item.get("phone_number"),
            nationality= item.get("nationality"),
            ticket_type= item.get("ticket_type"),
            flight= flight,
        )
        print(res_object)
        res_object.save()
    return HttpResponse(200)

#TODO: Normal staff view using the login