from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone

class Ram(models.Model):
    capacity = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=255)
    speed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.capacity}GB {self.manufacturer} RAM"

#USERS
class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)  # Assuming a maximum length of 15 for phone numbers
    password = models.CharField(max_length=128)
    profile = models.ImageField(upload_to='static/profiles/', null=True, blank=True)
    # latlong values
    latitude = models.CharField(null=True, blank=True, max_length=128)
    longitude = models.CharField(null=True, blank=True, max_length=128)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    # Add or change related_name for groups and user_permissions
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return self.email

# #DISASTERS

class Earthquake(models.Model):
    earthquake_key=models.AutoField(primary_key=True)
    richter=models.FloatField(null=True,blank=True)
    year=models.IntegerField()
    casualties=models.IntegerField(null=True,blank=True)
    loss=models.IntegerField(null=True,blank=True)
    #latlong values
    latitude_epicenter=models.FloatField(null=True,blank=True)
    longitude_epicenter=models.FloatField(null=True,blank=True)
    # epicenter = models.PointField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Flood(models.Model):
    FLOOD_CAUSES = [
        ('rainfall', 'Rainfall'),
        ('landslide', 'Landslide'),
        ('golf', 'Golf'),
        ('dam_failure', 'Dam Failure'),
        ('river_channel_changes', 'River Channel Changes'),
        ('other', 'Other'),
    ]
    flood_key=models.AutoField(primary_key=True)
    rainfall=models.FloatField(null=True,blank=True)
    year=models.IntegerField()
    casualties=models.IntegerField(null=True,blank=True)
    loss=models.IntegerField(null=True,blank=True)
    latitude_epicenter=models.FloatField(null=True,blank=True)
    longitude_epicenter=models.FloatField(null=True,blank=True)
    # epicenter = models.PointField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    cause = models.CharField(max_length=100, choices=FLOOD_CAUSES, default='rainfall')
    is_active = models.BooleanField(default=True)



class Glof(models.Model):
    GLOF_CAUSES= [
        ('avalanche', 'Avalanche'),
        ('earthquake', 'Earthquake'),
        ('dam_failure', 'Dam Failure'),
        ('other', 'Other'),
    ]
    glof_key=models.AutoField(primary_key=True)
    water_level=models.FloatField(null=True,blank=True)
    year=models.IntegerField()
    casualties=models.IntegerField(null=True,blank=True)
    cause = models.CharField(max_length=100, choices=GLOF_CAUSES, default='avalanche')
    loss=models.IntegerField(null=True,blank=True)
    latitude_epicenter=models.FloatField(null=True,blank=True)
    longitude_epicenter=models.FloatField(null=True,blank=True)
    # epicenter = models.PointField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Landslide(models.Model):
    LANDSLIDE_CAUSES= [
        ('earthquake', 'Earthquake'),
        ('rainfall', 'Rainfall'),
        ('soil_erosion', 'Soil Erosion'),
        ('other', 'Other'),
    ]
    landslide_key=models.AutoField(primary_key=True)
    year=models.IntegerField()
    casualties=models.IntegerField(null=True,blank=True)
    loss=models.IntegerField(null=True,blank=True)
    cause = models.CharField(max_length=100, choices=LANDSLIDE_CAUSES, default='rainfall')
    latitude_epicenter=models.FloatField(null=True,blank=True)
    longitude_epicenter=models.FloatField(null=True,blank=True)
    # epicenter = models.PointField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
