from django.db import models


class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.locationName


class Vehicle(models.Model):
    vehicleName = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    vehicleLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicleName
