from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render

from . import models
from .models import Earthquake, Flood, Glof, Landslide, User


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

        return redirect('signin')

    return render(request, 'signup.html')

def calculate_users_form(request):
    # Fetch all active floods from the database
    active_floods = Flood.objects.filter(is_active=True)

    # Create a dictionary to represent the response
    response_data = {'active_floods': []}

    # Iterate through each active flood
    for flood in active_floods:
        # Fetch all users from the database
        all_users = User.objects.all()

        # Convert flood coordinates to floats
        try:
            flood_lat = float(flood.latitude_epicenter)
            flood_lon = float(flood.longitude_epicenter)
        except ValueError:
            # Handle the case where the coordinates cannot be converted to float
            continue

        # Filter users within the radius of the flood using an if-else statement
        users_within_radius = [
            {
                'user_email': user.email,
                'latitude': user.latitude,
                'longitude': user.longitude
            }
            for user in all_users
            if (
                user.latitude and user.longitude and  # Check for non-empty values
                flood_lat - flood.radius <= float(user.latitude) <= flood_lat + flood.radius and
                flood_lon - flood.radius <= float(user.longitude) <= flood_lon + flood.radius
            )
        ]

        # Collect user information for the response
        users_info = {
            'epicenter_latitude': flood.latitude_epicenter,
            'epicenter_longitude': flood.longitude_epicenter,
            'radius': flood.radius,
            'users_within_radius': users_within_radius
        }

        # Append the information to the response
        response_data['active_floods'].append(users_info)

    # Return the response as JSON
    return JsonResponse(response_data)