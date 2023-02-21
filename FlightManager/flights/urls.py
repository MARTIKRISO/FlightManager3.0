from django.urls import path
from . import views

app_name = "flight"

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:pk>", views.book, name="book"),
    path("see_flights", views.seeflights, name="seeflights"),
    path("login", views.login, name="login"),
    path("checkout", views.checkout, name="checkout"),
    path("flightdata", views.flightdata, name="flightdata"),
    path("reserve", views.reserve, name="reserve"),

]