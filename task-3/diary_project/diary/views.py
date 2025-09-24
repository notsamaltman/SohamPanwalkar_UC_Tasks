from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages

def login(request):
    return render(request, 'diary/diary_template.html')

def register(request):
    return render(request, 'diary/diary_register.html')

def register_user(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        password = request.POST['password1']

        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        # Create user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            age=age,
            gender=gender
        )
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')
    return render(request, 'register')
