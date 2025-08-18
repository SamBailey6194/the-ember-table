from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from booking.models import Customer


# Create your models here.
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(
            user=instance,
            customer_fname=instance.first_name or "",
            customer_lname=instance.last_name or "",
            email=instance.email or "",
            phone=""
        )
