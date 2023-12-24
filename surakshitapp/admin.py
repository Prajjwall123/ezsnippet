from django.contrib import admin

# Register your models here.
from .models import Earthquake, Flood, Glof, Landslide, Ram, User

# admin.site.register(Ram)
admin.site.register(User)
admin.site.register(Earthquake)
admin.site.register(Flood)
admin.site.register(Landslide)
admin.site.register(Glof)

