from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from api.apps.api_auth.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import re


def register(request):   
    if request.method == "POST" and request.POST:
        password = request.POST['password']
        password_check = (len(password) >= 8, re.search(r'[A-Z]', password), re.search(r'[a-z]', password), re.search(r'\d', password), re.search(r'[!@#$%^&*?><]', password))
        if not all(password_check):
            return JsonResponse({"Error": "The password must contain letters in different case, symbols and numbers"})
        else:
            user = User.objects.filter(username=request.POST['username']).first()
            if not user:
                new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])                                                  
                new_user.save()
                user_profile = UserProfile()
                user_profile.user = new_user
                user_profile.save()
                return JsonResponse({"Success": "User have been registered"})
            else:
                return JsonResponse({"Error": "User already exists"})
    else:
        return render(request, 'auth_api/reg.html')


def user__login(request):
    if request.method == "POST" and request.POST:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            print(request.session)
            return JsonResponse({"Success": "You are welcome"})
        else:
            return JsonResponse({"Error": "Incorrect username or password"})
    else:
        return render(request, 'auth_api/login.html')


def status(request):
    if request.user.is_authenticated:
        return JsonResponse({"Status": "You are authenticated"})
    else:
        return JsonResponse({"Status": "You are not authenticated"})


def logout__view(request):
    logout(request)