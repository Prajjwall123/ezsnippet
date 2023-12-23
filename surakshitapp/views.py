import folium
import geocoder
from django.http import JsonResponse
from django.shortcuts import render
from folium import plugins

from .models import Earthquake, Flood, Glof
from .utils import bar_plot, flood_plot, glof_plot, plot, plot_pie


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

    # heatmap
    # data=Earthquake.objects.all()
    data_list = Earthquake.objects.exclude(latitude_epicenter=None, longitude_epicenter=None).values_list('latitude_epicenter', 'longitude_epicenter', 'richter')
    map1=folium.Map(location=[28,84],zoom_start=7)
    # data=[[28,84,3000],[28,91,2000]]
    plugins.HeatMap(data_list).add_to(map1)

    map1=map1._repr_html_()
    
    # Rest of the code remains unchanged
    return render(request, 'earthquake.html', {'chart': chart,'bar':bar,'map1':map1},)




from django.db.models import Min


def flood(request):
    # Retrieve data from the database
    causes_frequency = get_causes_frequency()
    # Pass data to the pie_chart function in utils.py
    pie = plot_pie(causes_frequency)
    min_rainfall_by_year = Flood.objects.values('year').annotate(min_rainfall=Min('rainfall'))

    # Extract years and corresponding minimum rainfall values
    years = [entry['year'] for entry in min_rainfall_by_year]
    min_rainfalls = [entry['min_rainfall'] for entry in min_rainfall_by_year]
    # Plot the data
    flood_chart = flood_plot(years, min_rainfalls)
    

    return render(request, 'flood.html', {'pie': pie,'flood_chart':flood_chart})


from collections import Counter


def get_causes_frequency():
    # Retrieve all causes from the database
    causes = Flood.objects.values_list('cause', flat=True)
    causes_frequency = Counter(causes)
    return causes_frequency


def glof(request):
    qs=Glof.objects.all()
    x=[x.water_level for x in qs]
    y=[y.year for y in qs]
    chart=glof_plot(y,x) 
    return render(request,'glof.html',{'chart':chart})

def landslide(request):
    return render(request,'landslide.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')
from django.http import JsonResponse
from django.shortcuts import render

from .models import Earthquake


def earthquake_alert(request):
    all_quakes = Earthquake.objects.all

    return render(request, 'alertearth.html', {'quakes': all_quakes})




def flood_alert(request):
    return render(request,'alertflood.html')

def glof_alert(request):
    return render(request,'alertglof.html')

def landslide_alert(request):
    return render(request,'alertland.html')


def get_model_data(request):
    # Fetch data from your model, for example:
    model_data = Earthquake.objects.all().values()  # Fetch all data from the model

    # Convert model data to a list of dictionaries
    data_list = list(model_data)

    return JsonResponse(data_list, safe=False)




