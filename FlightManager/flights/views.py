from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.forms.models import model_to_dict
from . import models
import json
from argon2 import PasswordHasher #Most secure hashing algo
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText


ph = PasswordHasher()

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
    ctx = {
        "data": data
    }
    return render(request, "flights/seeflights.html", ctx)

def login(request):
    if request.method == "GET":
        return render(request, "flights/login.html")
    else:
        return HttpResponseRedirect("/admin")
        #data = json.loads(request.POST.get("order"))

        # username = request.POST["username"]
        # password = request.POST["password"]

        # #TODO: Handle hashing and logging in
        # dbrecord = get_object_or_404(models.User, username=username)

        # hashedpassword = getattr(dbrecord, "password")
        # try:
        #    a = ph.verify(hashedpassword, password)
        #    if a:
        #         print("Pass correct!")
        #         session = models.SessionData(user = dbrecord)
        #         request.session["user"] = session
        #         return HttpResponseRedirect("/admin") #TODO: Create staff panel
                

        # except:
        #    # print("Pass wrong! Expected - got: " + str(hashedpassword), str(ph.hash(password)))
        #     return HttpResponseRedirect("/admin") #TODO: Make this better




        # return HttpResponse("OK")


def checkout(request):
    return render(request, "flights/checkout.html")

def flightdata(request):
    pk = request.GET.get("pk", None)
    flight = get_object_or_404(models.Flight, pk= pk)
    return HttpResponse(serializers.serialize("json", [flight, ]))

def reserve(request):
    order = str(request.POST.get('order'))
    print("Order: " + order)
    try:
        data = json.loads(order)
    except json.decoder.JSONDecodeError as e:
        return HttpResponse(200)


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
        res_object.save()
        send_email(model_to_dict(res_object))
        #print(res_object)
        
    
    return HttpResponse(200)

def createUserRecord(request):
    username = input("Username: ")
    password = ph.hash(input("Password: "))
    email = input("Email: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    EGN = input("EGN/SSN: ")
    address = input("Address: ")
    phone_number = input("Phone number: ")

    record = models.User( username= username, password = password, email = email, f_name = f_name,l_name = l_name, EGN =  EGN, address = address, phone_number = phone_number)
    record.save()
    return HttpResponse(200)
#TODO: Normal staff view using the login

def send_email(data):
    msg = MIMEMultipart()
    msg['From'] = 'mshkodrov3@gmail.com'
    msg['To'] = data["email"]
    msg['Subject'] = 'Confirmation for booking on flight ' + str(data["flight"])
    message = f"""
    Dear Sir or Madam,
    You are receiving this email to confirm your booking with Spas Airlines.
    Booking info:

    First Name: {data["f_name"]}
    Middle Name: {data["m_name"]}
    Last Name: {data["l_name"]}
    EGN: {data["EGN"]}
    Nationality: {data["nationality"]}
    ticket_type: {data["ticket_type"]}

    If the information is not correct, please contact us at contact@spasairlines.bg!


    Thank you for choosing us!
    """
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('mshkodrov3@gmail.com', 'gwimuxaworzrihve')

    mailserver.sendmail('mshkodrov3@gmail.com', data["email"], msg.as_string())

    mailserver.quit()
