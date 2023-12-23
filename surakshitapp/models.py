from django.db import models

from django.db import models

class Ram(models.Model):
    capacity = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=255)
    speed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.capacity}GB {self.manufacturer} RAM"
