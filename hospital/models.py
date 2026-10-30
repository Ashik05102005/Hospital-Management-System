from django.db import models

# Create your models here.
class Docters(models.Model) :
    name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    qualifictaion = models.CharField(max_length=100)
    avilabilty = models.CharField(max_length=100)
    consultation_fee = models.IntegerField()
    image = models.URLField(max_length=500)

class Patients(models.Model) :
    patient_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    appointment_date = models.DateField()
    status = models.CharField(max_length=100)