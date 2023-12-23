from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def alerts(request):
    return render(request,'alerts.html')

def earthquake(request):
    return render(request,'earthquake.html')

def flood(request):
    return render(request,'flood.html')

def glof(request):
    return render(request,'glof.html')

def landslide(request):
    return render(request,'landslide.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user with custom user model
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')  # Replace 'dashboard' with the URL name of your dashboard page
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        phone_number=request.POST['phone_number']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        email = request.POST['email']
        print(username, password, phone_number, latitude, longitude, email, name)

        myuser = User.objects.create_user(email=email, password=password, phone_number=phone_number, latitude=latitude, longitude=longitude, name=name)

        return redirect('login')

    return render(request, 'signup.html')
