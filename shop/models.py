from django.db import models

# Create your models here.
class Visitor(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitors: {self.count}"
    



class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    date = models.DateField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.payment_status.capitalize()} - {self.date}"