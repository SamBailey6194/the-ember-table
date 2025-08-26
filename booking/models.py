from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid


# Create models here
class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
        )
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'(^0\d{10}$)|(^\+?\d{7,15}$)',
                message="Enter a valid UK 11-digit number "
                "or an international number starting with +",
            )
        ]
        )
    email = models.EmailField()
    customer_fname = models.CharField(max_length=100)
    customer_lname = models.CharField(max_length=100)

    def __str__(self):
        if self.user:
            return f'{self.user.username}'
        return f'{self.customer_fname} {self.customer_lname} (Guest)'


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'Table {self.number} (Capacity: {self.capacity})'


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('unavailable', 'Unavailable'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='pending'
        )
    table = models.ForeignKey(
        Table, on_delete=models.SET_NULL, null=True, blank=True
        )
    reference_code = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
        )

    def __str__(self):
        return (
            f'Booking {self.reference_code} for '
            f'{self.customer} on {self.date} at {self.time}'
            )
