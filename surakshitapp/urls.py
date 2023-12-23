from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('alerts', views.alerts,name='alerts'),
    path('earthquake', views.earthquake,name='earthquake'),
    path('flood', views.flood,name='flood'),
    path('landslide', views.landslide,name='landslide'),
    path('glof', views.glof,name='glof'),
    
    path('earthquake-alert', views.get_model_data,name='get_model_data'),
    path('flood-alert', views.flood_alert,name='flood_alert'),
    path('landslide-alert', views.landslide_alert,name='landslide_alert'),
    path('glof-alert', views.glof_alert,name='glof_alert'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
]