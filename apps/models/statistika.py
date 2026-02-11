from django.db import models


class Statistics(models.Model):
    Patients = models.PositiveIntegerField(default=0)
    Customer = models.PositiveIntegerField(default=0)
    # Certified = models.PositiveIntegerField(default=0)
    # Pharmacy = models.PositiveIntegerField(default=0)
    Years = models.PositiveIntegerField(default=0)
    working_hours = models.CharField(max_length=50, default="24/7", verbose_name="working hours")
