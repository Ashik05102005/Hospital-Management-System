from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Docters(models.Model) :
    id = models.BigAutoField( primary_key=True )
    name = models.CharField(max_length=80)
    department = models.CharField(max_length=100 )
    experience = models.IntegerField()
    qualifictaion = models.CharField(max_length=100)
    avilabilty = models.CharField(max_length=100)
    consultation_fee = models.IntegerField()
    image = models.URLField(max_length=500)

STATUS_CHOICES = [
    ("COMPLETED", "Completed"),
    ("CONFIRMED", "Confirmed"),
    ("PENDING", "Pending"),
]
GENDER_CHOICES = [
    ("MALE", "male"),
    ("FEMALE", "female")
]


class Patients(models.Model) :
    patient_id = models.CharField(max_length=10 , primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    department = models.CharField(max_length=100)
    appointment_date = models.DateField()
    status = models.CharField(max_length=100 ,
                              choices=STATUS_CHOICES ,
                              default='PENDING')


class Profile(models.Model) :
    user = models.OneToOneField(
        User ,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=15) 
    address= models.CharField(max_length=100)