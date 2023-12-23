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

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        phone_number = request.POST['phone_number']  # Change from 'email' to 'phone_number'
        
        print(username, password, name, latitude, longitude, phone_number)

        myuser = User.objects.create_user(phone_number=phone_number, password=password, name=name, latitude=latitude, longitude=longitude)

        return redirect('login')

    return render(request, 'signup.html')
