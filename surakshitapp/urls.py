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
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
]