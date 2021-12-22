from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth


# Create your views here.

def registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is currently being used')
                    return redirect('register')
                else:
                    user= User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    user = authenticate(username= username, password=password2)
                    if user is not None:
                        print('User is authenticated')
                        login(request)
                        messages.success(request, 'You are now registered and can log in')
                        return redirect('gallery')
                    else:
                        print('user is NOT authenticated')
                        return redirect('register')
        else:
            messages.error(request, 'Either username/passwords did not match')
            return redirect('register')

    else:
        return render(request, 'accounts/registeration.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Succesfully logged in')
            return redirect('gallery')
        else:
            messages.error(request, 'Either incorrect username or password. Try again')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('gallery')
