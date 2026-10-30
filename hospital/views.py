from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
def register_view(request) :

    form = RegisterForm()

    if request.method == "POST" :
        form = RegisterForm(request.POST)

        if form.is_valid() :
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


    # if request.method == "POST" :
    #     print(request.POST)
    #     username = request.POST.get("username")
    #     email = request.POST.get("email")
    #     password = request.POST.get("password")

    #     if User.objects.filter(username = username).exists():
    #         return render(request , "register.html" , {"error" : "User already exists"})

    #     User.objects.create_user(
    #         username = username ,
    #         email=email ,
    #         password = password
    #     )

    #     return redirect("home")

    # return render(request , "register.html")

# def login_view(request) :
#     if request.method == "POST" :

#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(
#             request ,
#             username = username ,
#             password = password
#         )

#         if user is not None :
#             login(request , user)
#             request.session["username"] = username
#             return redirect('home')

#         else :
#             return render(request , "login.html" , {"error" : "Invalid Username or Password"})

#     return render(request,"login.html")

# def logout_view(request):
#     if request.method == 'POST':

#         logout(request)

#         return redirect('login')

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
    doctors = [
    {
        "name": "Dr. Arun Kumar",
        "department": "Cardiology",
        "experience": 12,
        "qualification": "MBBS, MD Cardiology",
        "availability": "Monday–Friday",
        "consultation_fee": 800,
        "image": "https://images.openai.com/static-rsc-4/v8jI3dUD0vbDB4cQj1-RWbxmKUAJK7scECNumfrGOKH9S-oHSK_8I0krJzeXcBrDpKb24GYkzmSwoDCR4aCYVER9cziAn9_tYJnGQuH69F3LiWIA1HQogF7Df7iB3kBYeCC1NuWbV4S4t-HacLoZQHR7lfHJwZc5Px9tzn00WtM?purpose=inline",
    },
    {
        "name": "Dr. Priya Menon",
        "department": "Pediatrics",
        "experience": 8,
        "qualification": "MBBS, MD Pediatrics",
        "availability": "Monday–Saturday",
        "consultation_fee": 600,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbFzAXvdTbIVN5f9OH1QX1DJrDndX2Junh1dYw-o4Xww&s=10",
        # "image": "data:image/webp;base64,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",
    },
    {
        "name": "Dr. Mohammed Salim",
        "department": "Orthopedics",
        "experience": 10,
        "qualification": "MBBS, MS Orthopedics",
        "availability": "Tuesday–Saturday",
        "consultation_fee": 700,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFst3Fbr_AtXAWfnF6IOIwgt5WGrRbll2alzbvcpkewg&s=10",
    },
    ]
    return render(request , "doctors.html" , {"doctors" : doctors})

@login_required
def patients(request):
    patients = [
    {
        "patient_id": "P001",
        "name": "Rahul Das",
        "age": 28,
        "gender": "Male",
        "department": "Cardiology",
        "appointment_date": "28 Oct 2026",
        "status": "Confirmed"
    },
    {
        "patient_id": "P002",
        "name": "Anjali Nair",
        "age": 35,
        "gender": "Female",
        "department": "Pediatrics",
        "appointment_date": "29 Oct 2026",
        "status": "Pending"
    },
    {
        "patient_id": "P003",
        "name": "Nikhil Raj",
        "age": 42,
        "gender": "Male",
        "department": "Orthopedics",
        "appointment_date": "30 Oct 2026",
        "status": "Completed"
    },
    {
        "patient_id": "P004",
        "name": "Sneha Thomas",
        "age": 24,
        "gender": "Female",
        "department": "General Medicine",
        "appointment_date": "31 Oct 2026",
        "status": "Confirmed"
    },
    {
        "patient_id": "P005",
        "name": "Farhan Ali",
        "age": 50,
        "gender": "Male",
        "department": "Cardiology",
        "appointment_date": "1 Nov 2026",
        "status": "Pending"
    }
    ]
    return render(request , "patients.html" , {"patients" : patients})