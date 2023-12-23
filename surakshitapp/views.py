from django.http import JsonResponse
from django.shortcuts import render
from . models import Earthquake
from .utils import plot, bar_plot

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def alerts(request):
    return render(request,'alerts.html')

def earthquake(request):
    qs = Earthquake.objects.all()

# Create a dictionary to store the maximum Richter scale for each year
    max_richter_by_year = {}

    # Iterate through the queryset to find the maximum Richter scale for each year
    for quake in qs:
        year = quake.year
        richter = quake.richter

        # Update the maximum Richter scale for the year if a higher value is found
        if year in max_richter_by_year:
            max_richter_by_year[year] = max(max_richter_by_year[year], richter)
        else:
            max_richter_by_year[year] = richter

    # Extract years and corresponding maximum Richter scales
    x = list(max_richter_by_year.keys())
    y = list(max_richter_by_year.values())

    # Plot the data
    chart = plot(x, y)

    # ========================================
    # Create a dictionary to store the sum of casualties for each year
    casualties_by_year = {}

    # Iterate through the queryset to sum casualties for each year
    for quake in qs:
        year = quake.year
        casualties = quake.casualties

        # Update the sum of casualties for the year
        if year in casualties_by_year:
            casualties_by_year[year] += casualties
        else:
            casualties_by_year[year] = casualties

    # Extract years and corresponding total casualties
    x = list(casualties_by_year.keys())
    y = list(casualties_by_year.values())

    # Plot the bar graph
    bar = bar_plot(x, y)

    # Rest of the code remains unchanged
    return render(request, 'earthquake.html', {'chart': chart,'bar':bar})





def flood(request):
    return render(request,'flood.html')

def glof(request):
    return render(request,'glof.html')

def landslide(request):
    return render(request,'landslide.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')


def earthquake_alert(request):
    return render(request,'alertearth.html')

def flood_alert(request):
    return render(request,'alertflood.html')

def glof_alert(request):
    return render(request,'alertglof.html')

def landslide_alert(request):
    return render(request,'alertland.html')





