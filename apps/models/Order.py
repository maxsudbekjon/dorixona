
from django.db import models

from apps.models.blogservise import Service


class ContactRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)



    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class RefillOrder(models.Model):
    DELIVERY_CHOICES = (
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    delivery_type = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='delivery')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.first_name}"


class RefillItem(models.Model):
    order = models.ForeignKey(RefillOrder, on_delete=models.CASCADE, related_name='refill_items')
    rx_number = models.CharField(max_length=50)


class ExtraItem(models.Model):
    order = models.ForeignKey(RefillOrder, on_delete=models.CASCADE, related_name='extra_items')
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
