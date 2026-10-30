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



    modified:    
        modified:   hospital/__pycache__/models.cpython-313.pyc
        modified:   hospital/__pycache__/urls.cpython-313.pyc
        modified:   hospital/__pycache__/views.cpython-313.pyc
        modified:   hospital/models.py
        modified:   hospital/templates/home.html
        modified:   hospital/templates/login.html
        modified:   hospital/templates/register.html
        modified:   hospital/templates/registration/login.html
          hospital/views.py
          hospital_management/__pycache__/settings.cpython-313.pyc
          hospital_management/settings.py