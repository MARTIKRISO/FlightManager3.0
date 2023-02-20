from django.urls import path
from . import views

app_name = "flight"

urlpatterns = [
    path("", views.index, name="index"),
    path("book_a_flight", views.bookflight, name="bookflight"),
    path("see_flights", views.seeflights, name="seeflights"),
    path("login", views.login, name="login"),
]