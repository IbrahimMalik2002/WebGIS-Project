from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .models import user_info
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_protect


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    return render(request, 'booking.html')


def contact(request):
    return render(request, 'contact.html')


def Login(request):
    return render(request, 'Login.html')


def maps(request):
    return render(request, 'maps.html')


def registration_success(request):
    return render(request, 'registration_success.html')


def logout(request):
    return render(request, 'logout.html')


def register(request):
    if request.method == 'POST':
        new_username = request.POST['new_username']
        new_email = request.POST['new_email']
        new_password = request.POST['new_password']

        # Create a new user_info object
        user = user_info(username=new_username,
                         email=new_email, password=new_password)

        # Save the user_info object to the database
        user.save()

        # Redirect to a success page or login page
        return redirect('registration_success')

    return render(request, 'register.html')


@login_required
@csrf_protect
def loggingin(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        print(f"Username: {username1}, Password: {password1}")

        user = auth.authenticate(username=username1, password=password1)
        if user is not None:
            print("Authentication successful")
            auth.login(request, user)
            return redirect('index.html')  # Redirect to the index view
        else:
            print("Authentication failed")
            # Redirect back to the login page
            return redirect('Login.html')
    return render(request, 'Login.html')


def login_view(request):
    return render(request, 'Login.html')
