from django import forms 
from .models import Patients , Docters , Profile , CustomUser
from django.contrib.auth.forms import UserCreationForm




class RegisterForm (UserCreationForm):

    class Meta :
        model = CustomUser 
        fields = [
            'username',
            'email',
            'phone',
            'address',
            'password1',
            'password2'
        ]

    

class Patients_Form(forms.ModelForm) :

    class Meta :
        model = Patients
        fields = "__all__"

class Doctor_Form(forms.ModelForm) :

    class Meta :
        model = Docters 
        fields = '__all__'

class ProfileForm(forms.ModelForm):

    class Meta :
        model = Profile
        fields = ['phone' , 'address']