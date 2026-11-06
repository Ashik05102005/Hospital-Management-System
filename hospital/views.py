from django.shortcuts import render , redirect
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .forms import Patients_Form , Doctor_Form , ProfileForm
from .models import Patients , Docters ,Profile
from django.db.models import F , Value , Sum , Avg


# Create your views here.
def register_view(request) :

    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('home')
    else :
        form = RegisterForm()

    return render(request , 'register.html' , {'form' : form})


def home(request) :
    print(request.GET)
    # print("request",request.SESSIONS)
    
    response = render(request , "home.html" )
    return response


@login_required
def doctors(request) :
    doctors = Docters.objects.all()
    text_dict = Docters.objects.values()
    print(text_dict)

    return render(request , "doctors.html" , {"doctors" : doctors})

@login_required
def patients(request):
    patients = Patients.objects.all()
    # print(patients)
    return render(request , "patients.html" , {"patients" : patients})

def patient_register(request) :

    if request.method == "POST" :

        form = Patients_Form(request.POST)

        if form.is_valid() :

            form.save()

            return redirect('patients')

    else :

        form = Patients_Form()

    return render(request , 'patient_register.html' , {"form" : form})


def doctor_register(request) :
    form = Doctor_Form()
    if request.method == 'POST' :
        form = Doctor_Form(request.POST)

        if form.is_valid() :

            form.save()
             
            return redirect('doctors')

       

    return render(request , 'doctor_register.html' , {"form" : form})

@login_required
def profile(request):
    if not Profile.objects.filter(user_id = request.user.id).exists():
        if request.method == 'POST' :
            form = ProfileForm(request.POST)

            if form.is_valid() :
                profile_data =form.save(commit=False)

                profile_data.user = request.user

                profile_data.save()

                # return redirect('home')
        else :
            form = ProfileForm()

        return render(request , 'profile.html' , {"form" : form})
    else:
        data = Profile.objects.get(user_id=  request.user.id)
        print(data)
    return render(request , 'profile.html' , {"data" : data})

def test(request) :
    if request.method == 'POST' :
        print(request.POST)
    doctor = Docters.objects.get(id = 1)
    doctor_patients = doctor.patients.all()

    doctor_new = Docters.objects.annotate(
        new_consultation_fee = F('consultation_fee') + Value(200)
    )

    total_consultation_fee = Docters.objects.aggregate(
        total_consultation_fee = Sum('consultation_fee')
    )

    avarage_consultation_fee = Docters.objects.aggregate(
        avarage_consultation_fee = Avg('consultation_fee')
    )
    print(total_consultation_fee)
    print(avarage_consultation_fee)

    return render(request , 'test.html' ,{'doctor':doctor,"doctor_patients" : doctor_patients , 
                                          'doctor_new' : doctor_new  , 'total_consultation_fee' : total_consultation_fee ,
                                          'avarage_consultation_fee' : avarage_consultation_fee})



