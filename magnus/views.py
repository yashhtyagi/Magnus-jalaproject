from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@csrf_exempt
def userSession(request):
    if request.method == 'POST':
    
        username = request.POST.get('email')
        password = request.POST.get('password')

        try: 
            user = User.objects.get(email=username)

            if user.check_password(password):
                login(request, user)
                return redirect('Home/')
            else:
                messages.error(request,'Email Or Password is Incorrect')
                return redirect('/')

        except User.DoesNotExist:
            messages.error(request, 'User Does Not Found Contact Admin')   
            return redirect('/')
    
    return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('/')


def forgotpass(request):
    return render(request, 'forgot.html')