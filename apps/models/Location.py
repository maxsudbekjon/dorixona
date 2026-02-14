from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=255) 
    address = models.CharField(max_length=255) 
    phone = models.CharField(max_length=50) 
    fax = models.CharField(max_length=50, blank=True, null=True) 
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class WorkHour(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hours')
    day_range = models.CharField(max_length=100) 
    open_time = models.TimeField(null=True, blank=True) 
    close_time = models.TimeField(null=True, blank=True) 
    is_closed = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.location.title} - {self.day_range}"