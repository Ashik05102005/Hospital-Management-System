from django.shortcuts import render , redirect
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .forms import Patients_Form , Doctor_Form , ProfileForm
from .models import Patients , Docters ,Profile

# Create your views here.
def register_view(request) :

    form = RegisterForm()

    if request.method == "POST" :
        form = RegisterForm(request.POST)

        if form.is_valid() :
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username = username ).exists() :
                return render(request , 'register.html' , {"form" : form ,"error" : "username already exists"})
            
            if User.objects.filter(email = email ).exists() :
                return render(request , 'register.html' , {"form" : form ,"error" : "email already exists"})

            User.objects.create_user(
                username= username ,
                password=password ,
                email=email ,
            )

            return redirect("login")

    return render(request , 'register.html' , {"form" : form}) 




def home(request) :
    # print("request",request.SESSIONS)
    username = request.session.get("username" , "empty")
    print(username)
    visits = int(request.COOKIES.get('visits' , 0))
    visits += 1
    response = render(request , "home.html" , {"visits" : visits})
    response.set_cookie('visits' , visits)
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

                return redirect('home')
        else :
            form = ProfileForm()

        return render(request , 'profile.html' , {"form" : form})
    else:
        data = Profile.objects.get(user_id=  request.user.id)
        print(data)
        return render(request , 'profile.html' , {"data" : data})



