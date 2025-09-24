import random
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

def login(request):
    return render(request, 'diary/diary_template.html')

def register(request):
    return render(request, 'diary/diary_register.html')

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  
            username = data.get('username')
            email = data.get('email')
            age = data.get('age')
            gender = data.get('gender')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'})

        # Validate
        if not username or not email or not password or not age or not gender:
            print("error 1")
            return JsonResponse({'success': False, 'error': 'All fields are required.'})

        if CustomUser.objects.filter(username=username).exists():
            print("error 2")
            return JsonResponse({'success': False, 'error': 'Username already taken.'})

        if CustomUser.objects.filter(email=email).exists():
            print("error 3 ")
            return JsonResponse({'success': False, 'error': 'Email already registered.'})
            

        code = str(random.randint(100000, 999999))

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            age=age,
            gender=gender,
            is_active=False,
            verification_code=code
        )

        send_mail(
            subject="Verify your email",
            message=f"Your verification code is: {code}",
            from_email="diaryappbysoham@gmail.com",
            recipient_list=[email],
        )

        request.session['user_id'] = user.id  
        return redirect('diary_verifyemail.html')

    return render(request, 'register.html')

def verify_code(request):
    if request.method == "POST":
        email = request.POST.get("email")
        entered_code = request.POST.get("code")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect("diary_verifyemail.html")

        if user.verification_code == entered_code:
            user.is_active = True
            user.verification_code = None
            user.save()
            messages.success(request, "Email verified! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Invalid verification code.")
            return redirect("diary_verifyemail.html")

    return render(request, "diary_verifyemail.html")

