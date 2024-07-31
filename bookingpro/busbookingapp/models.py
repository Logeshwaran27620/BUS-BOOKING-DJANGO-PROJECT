from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class busdetails(models.Model):
       busname=models.CharField(max_length=23)
       depaturetime=models.CharField(max_length=30)
       arrivaltime=models.CharField(max_length=40)
       traveltime=models.CharField(max_length=23)
       price=models.CharField(max_length=30)
       bustype=models.CharField(max_length=40)
       busratting=models.CharField(max_length=23)
       bustotalratting=models.CharField(max_length=30)
       depaturelocation=models.CharField(max_length=40)
       arrivallocation=models.CharField(max_length=23)
       windowseat=models.CharField(max_length=30)
       seatavailable=models.CharField(max_length=40)
       is_active=models.BooleanField(default=True)

def __str__(self):
        return self.busname

class busmduchn(models.Model):
       busname=models.CharField(max_length=23)
       depaturetime=models.CharField(max_length=30)
       arrivaltime=models.CharField(max_length=40)
       traveltime=models.CharField(max_length=23)
       price=models.CharField(max_length=30)
       bustype=models.CharField(max_length=40)
       busratting=models.CharField(max_length=23)
       bustotalratting=models.CharField(max_length=30)
       depaturelocation=models.CharField(max_length=40)
       arrivallocation=models.CharField(max_length=23)
       windowseat=models.CharField(max_length=30)
       seatavailable=models.CharField(max_length=40)
       is_active=models.BooleanField(default=True)

def __str__(self):
        return self.busname

class buschndpm(models.Model):
       busname=models.CharField(max_length=23)
       depaturetime=models.CharField(max_length=30)
       arrivaltime=models.CharField(max_length=40)
       traveltime=models.CharField(max_length=23)
       price=models.CharField(max_length=30)
       bustype=models.CharField(max_length=40)
       busratting=models.CharField(max_length=23)
       bustotalratting=models.CharField(max_length=30)
       depaturelocation=models.CharField(max_length=40)
       arrivallocation=models.CharField(max_length=23)
       windowseat=models.CharField(max_length=30)
       seatavailable=models.CharField(max_length=40)
       is_active=models.BooleanField(default=True)

def __str__(self):
        return self.busname

class busdpmchn(models.Model):
       busname=models.CharField(max_length=23)
       depaturetime=models.CharField(max_length=30)
       arrivaltime=models.CharField(max_length=40)
       traveltime=models.CharField(max_length=23)
       price=models.CharField(max_length=30)
       bustype=models.CharField(max_length=40)
       busratting=models.CharField(max_length=23)
       bustotalratting=models.CharField(max_length=30)
       depaturelocation=models.CharField(max_length=40)
       arrivallocation=models.CharField(max_length=23)
       windowseat=models.CharField(max_length=30)
       seatavailable=models.CharField(max_length=40)
       is_active=models.BooleanField(default=True)

def __str__(self):
        return self.busname

class passengerdetailsforms1(models.Model):
    username=models.CharField(max_length=40)
    usernumber=models.CharField(max_length=23)
    useremail=models.CharField(max_length=30)
    userage=models.CharField(max_length=40)
    usergender=models.CharField(max_length=23)
    userchild=models.CharField(max_length=40)
    userid=models.CharField(max_length=23)
    userboardingpoint=models.CharField(max_length=30)
    userdropingpoint=models.CharField(max_length=40)
    useridtype=models.CharField(max_length=23)
    userseat=models.CharField(max_length=40)




class contactdetails(models.Model):
    username=models.CharField(max_length=40)
    useremail=models.CharField(max_length=30)
    usernumber=models.CharField(max_length=23)
    
# models.py
from django.db import models

class Bookingselection(models.Model):
    ORIGIN_CHOICES = [
        ('CHENNAI', 'Chennai'),
        ('COIMBATORE', 'Coimbatore'),
        ('MADURAI', 'Madurai'),
        ('TIRUCHY', 'Tiruchy'),
        ('DHARAPURAM', 'Dharapuram'),
    ]
    
    DESTINATION_CHOICES = [
        ('CHENNAI', 'Chennai'),
        ('COIMBATORE', 'Coimbatore'),
        ('MADURAI', 'Madurai'),
        ('TIRUCHY', 'Tiruchy'),
        ('DHARAPURAM', 'Dharapuram'),
    ]
    
    origin = models.CharField(max_length=20, choices=ORIGIN_CHOICES)
    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES)
    passengers = models.PositiveIntegerField()
    depart = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
        return f'{self.origin} to {self.destination} on {self.depart}'




  




    


   
