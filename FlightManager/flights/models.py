from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    EGN = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    role = models.CharField(max_length=10, default="staff")

    def __str__(self):
        return f"{self.pk} - {self.username} - {self.fname} {self.lname} - {self.role}"


class Flight(models.Model):
    from_location = models.CharField(max_length=20)
    to_location = models.CharField(max_length=20)
    takeoff_time = models.TimeField()
    landing_time = models.TimeField()
    plane_type = models.CharField(max_length=20)
    plane_id = models.CharField(max_length=20)
    pilot_name = models.CharField(max_length=40)
    normal_ticket_count = models.IntegerField()
    business_ticket_count = models.IntegerField()
    normal_ticket_price = models.DecimalField(decimal_places=2, max_digits=5)
    business_ticket_price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.pk} - {self.from_location} -> {self.to_location} - {self.plane_id}"
    
class Reservation(models.Model):
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    EGN = models.CharField(max_length=12)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    nationality = models.CharField(max_length=2)
    ticket_type = models.CharField(max_length=8)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)