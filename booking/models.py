from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    """
    Controls the logging in and creation of account
    or a customer can create a guest account to make a booking
    """
    username = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    phone = models.CharField(max_length=15)
    is_guest = models.BooleanField(default=False)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.username.get_full_name()} (Registered)"
        return f"Guest ({self.phone})"


class UserAction(models.Model):
    """
    Reusable model to determine which staff members made an action
    against the bookings
    """
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
        )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Action by {self.user} at {self.timestamp}"


class Table(models.Model):
    """
    Allows admins to set the table numbers and their capacities.
    Helping the admins to assign tables properly
    """
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return (
            f"Table {self.number} (Seats {self.capacity})"
            )


class Booking(models.Model):
    """
    Booking form for customers to make a booking.
    """
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("unavailable", "Unavailable"),
        ("seated", "Seated"),
        ("cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    party_size = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending"
        )
    reference_code = models.CharField(max_length=12, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    tables = models.ManyToManyField(
        Table, through='TableAssignment', related_name='bookings'
        )

    def __str__(self):
        return f"{self.customer} | {self.date} {self.time}"


class BookingManagement(models.Model):
    """
    Admins can control the Bookings
    """
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='management_logs'
        )
    status = models.CharField(max_length=20, choices=Booking.STATUS_CHOICES)
    notes = models.TextField(blank=True, null=True)
    action = models.OneToOneField('UserAction', on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Management for Booking {self.booking.reference_code} status "
            f"{self.status} updated by {self.action.user} at "
            f"{self.action.timestamp}"
            )


class TableAssignment(models.Model):
    """
    Admins can assign a table to a booking. This helps with the many to many
    relationship between booking and table.
    """
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    action = models.OneToOneField(
        UserAction, on_delete=models.CASCADE,
        help_text="Tracks which staff user made this specific change"
        )

    class Meta:
        unique_together = ('booking', 'table')

    def __str__(self):
        return (
            f"Table {self.table.number} assigned to Booking "
            f"{self.booking.reference_code} updated by {self.action.user} at "
            f"{self.action.timestamp}"
            )
