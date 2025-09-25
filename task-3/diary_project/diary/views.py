import random
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    return render(request, 'diary/diary_template.html')

@csrf_exempt
@login_required(login_url='/login/')
def home(request):
    return render(request, 'diary/diary_home.html')

def register(request):
    return render(request, 'diary/diary_register.html')

def verify_code_page(request):
    if 'user_id' not in request.session:
        return redirect('register')
    return render(request, 'diary/diary_verifyemail.html')

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
        return JsonResponse({'success':True})

    return render(request, 'register.html')
@csrf_exempt
def verify_code(request):
    if request.method == "POST":
        data = json.loads(request.body)
        entered_code = data.get("code")
        email=data.get("email")
        if not email:
            return JsonResponse({'success': False, 'error': 'Session expired. Please register again.'})

        try:
            user = CustomUser.objects.get(email=email)  
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'})

        if user.verification_code == entered_code:
            user.is_active = True
            user.verification_code = None
            user.save()
            return JsonResponse({'success': True, 'message': 'Email verified!'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid code!'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'})

        if not username or not password:
            return JsonResponse({'success': False, 'error': 'All fields are required'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({'success': True, 'username': user.username})
            else:
                return JsonResponse({'success': False, 'error': 'Account not verified'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

