from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import BookingManagement, TableAssignment, UserAction


@receiver(pre_save, sender=BookingManagement)
def create_user_action_for_booking_status(sender, instance, **kwargs):
    """
    Automates the user action model for the booking management
    """
    if not instance.pk:
        if not instance.action_id:
            instance.action = UserAction.objects.create(
                user=instance.user, timestamp=instance.timestamp
                )


@receiver(pre_save, sender=TableAssignment)
def create_user_action_for_table_assignment(sender, instance, **kwargs):
    """
    Automates the user action model for the table assignment
    """
    if not instance.pk:
        if not instance.action_id:
            instance.action = UserAction.objects.create(
                user=instance.user, timestamp=instance.timestamp
                )
