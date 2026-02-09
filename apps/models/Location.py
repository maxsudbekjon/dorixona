from django.db import models



class Location(models.Model):
    title = models.CharField(max_length=255) # Figma: "First Core Pharmacy – New York"
    address = models.CharField(max_length=255) # Figma: "123 Main Street..."
    phone = models.CharField(max_length=50) # Figma: Phone
    fax = models.CharField(max_length=50, blank=True, null=True) # Figma: Fax
    # Qo'lyozmada bor, xaritada ko'rsatish uchun kerak:
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    google_map_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# 6. WorkDay (Ish vaqtlari)
class WorkHour(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hours')
    day_range = models.CharField(max_length=100) # Masalan: "Monday – Friday" yoki "Saturday"
    open_time = models.TimeField(null=True, blank=True) # 8:00 AM
    close_time = models.TimeField(null=True, blank=True) # 7:00 PM
    is_closed = models.BooleanField(default=False) # "Sunday: Closed" uchun

    def __str__(self):
        return f"{self.location.title} - {self.day_range}"