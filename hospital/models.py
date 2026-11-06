from django.db import models
from django.conf import settings
from django.contrib.auth.models import User , AbstractUser

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

    def __str__(self):
        return self.name

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

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    department = models.CharField(max_length=100)
    docter = models.ForeignKey(
        Docters ,
        on_delete=models.CASCADE ,
        related_name='patients'
    )
    appointment_date = models.DateField()
    status = models.CharField(max_length=100 ,
                              choices=STATUS_CHOICES ,
                              default='PENDING')


class Profile(models.Model) :
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL ,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=15) 
    address= models.CharField(max_length=100)


class CustomUser(AbstractUser) :
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True , null=True )
    country = models.CharField(max_length=100 , null=True , blank=True)
    date_of_birth = models.DateField(blank=True , null= True)

