from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory,
                                 on_delete=models.CASCADE,
                                 related_name='services',
                                 blank=True,
                                 null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    name = models.CharField(max_length=255)  # Figma: "U.S. Food and Drug Administration"
    url = models.URLField()  # Figma: "www.fda.gov"

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)  # Figma: "Understanding Your Medications..."
    image = models.ImageField(upload_to='blog/')  # Figma: Rasm
    created_at = models.DateField()  # Figma: "Jan 11, 2026"
    description = models.TextField()  # Postning ichki matni

    def __str__(self):
        return self.title


class Review(models.Model):
    full_name = models.CharField(max_length=100)  # Figma: "Emily Carter"
    avatar = models.ImageField(upload_to='reviews/', blank=True, null=True)  # Figma: User rasmi
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  # Figma: Yulduzchalar (1 dan 5 gacha)
    message = models.TextField()  # Figma: "Friendly staff and fast service..."

    def __str__(self):
        return f"{self.full_name} ({self.rating} stars)"
