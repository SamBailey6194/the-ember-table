from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from booking.models import Customer, Booking


# Create your models here.
@receiver(post_delete, sender=User)
def delete_customer_and_bookings(sender, instance, **kwargs):
    try:
        customer = Customer.objects.get(user=instance)
        Booking.objects.filter(customer=customer).delete()
        customer.delete()
    except Customer.DoesNotExist:
        pass
