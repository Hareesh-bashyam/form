from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import User

# Create your views here.
def home(request):
    return render(request,'login.html')
    
def signup(request):
    return render(request,'singup.html')

def signup_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        # Save user (with hashed password)
        User.objects.create(
            full_name=full_name,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "Account created successfully! Please login.")
        return redirect("home")

    return render(request, "signup.html")
    
def login_view(request):
    if request.method == "POST":
            email = request.POST.get("email").strip()
            password = request.POST.get("password").strip()
            
            # Try to fetch user by email
            user_name = User.objects.filter(email=email).first()
            if user_name:
                if check_password(password, user_name.password):
                    return render(request,'home.html',{"user_name": user_name})
                else:
                    messages.error(request, "Incorrect password")
            else:
                messages.error(request, "User not found")
    return render(request, "login.html")    