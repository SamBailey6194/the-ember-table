from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking


# Create your signals here
@receiver(post_save, sender=Booking)
def booking_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'Booking created: {instance.reference_code}')
