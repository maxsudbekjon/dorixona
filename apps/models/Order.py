
from django.db import models

from apps.models.blogservise import Service


class ContactRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)  # Qo'shimcha xabar uchun
    want_delivery = models.BooleanField(default=False)  # Checkbox: "Yes, I want free pick-up..."

    # Qo'lyozmadagi "service" maydoni (ixtiyoriy)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# 8. Refill Order (Dori buyurtma qilish - Murakkab forma)
# Figma: "Refill Your Prescription"
class RefillOrder(models.Model):
    DELIVERY_CHOICES = (
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    )

    # Patient Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    # Delivery Type
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='delivery')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.first_name}"


# Retsept raqamlari (One-to-Many)
class RefillItem(models.Model):
    order = models.ForeignKey(RefillOrder, on_delete=models.CASCADE, related_name='refill_items')
    rx_number = models.CharField(max_length=50)  # Figma: "Enter RX refill number"


# Qo'shimcha narsalar (One-to-Many)
class ExtraItem(models.Model):
    order = models.ForeignKey(RefillOrder, on_delete=models.CASCADE, related_name='extra_items')
    name = models.CharField(max_length=255)  # Figma: "Enter name here"
    quantity = models.PositiveIntegerField(default=1)  # Figma: "Enter quantity here"
