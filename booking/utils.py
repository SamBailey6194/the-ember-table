from django.core.mail import send_mail
from datetime import datetime


# Create your utils here
def format_booking_date(dt):
    return datetime.strftime('%Y-%m-%d')


def generate_reference_code():
    import uuid
    return str(uuid.uuid4())


def send_status_email(booking):
    """
    Send email to the customer based on booking status.
    Handles both registered and guest customers.
    """
    first_name = getattr(booking.customer, 'first_name', None)
    if not first_name:
        first_name = getattr(booking.customer, 'customer_fname', 'Customer')

    if not getattr(booking.customer, 'email', None):
        return

    subject = None
    message = None

    if booking.status == "pending":
        subject = f"Booking Pending - Ref: {booking.reference_code}"
        message = (
            f"Dear {first_name},\n\n"
            "Thank you for sending a booking request to The Ember Table! "
            f"We will seek to confirm your booking asap for {booking.date} at "
            f"{booking.time}.\nYour booking reference code is "
            f"{booking.reference_code}. "
            "You can use this to edit your booking if you need to.\n\n"
            "Kind Regards, \nThe Ember Table Team"
        )
    elif booking.status == "confirmed":
        subject = f"Booking Confirmed - Ref: {booking.reference_code}"
        message = (
            f"Dear {first_name},\n\n"
            "Thank you for booking with The Ember Table! "
            f"Your reservation on {booking.date} at {booking.time} "
            "has been confirmed.\n\n"
            "We look forward to welcoming you!\n\n"
            "Kind Regards, \nThe Ember Table Team"
        )
    elif booking.status == "unavailable":
        subject = f"Booking Unavailable - Ref: {booking.reference_code}"
        message = (
            f"Dear {first_name},\n\n"
            "We regret to inform you that your requested booking "
            f"for {booking.date} at {booking.time} is unavailable.\n"
            "We apologise for any inconvenience caused.\n\n"
            "Please fill out the form again to find another suitable time.\n\n"
            "Kind Regards, \nThe Ember Table Team"
        )
    elif booking.status == "cancelled":
        subject = f"Booking Cancelled - Ref: {booking.reference_code}"
        message = (
            f"Dear {first_name},\n\n"
            "Thank you for booking with The Ember Table! "
            f"Your reservation on {booking.date} at {booking.time} "
            "has been cancelled as requested.\n"
            "We are sad that you had to cancel. If you would like to "
            "book for a different time please use the form.\n\n"
            "Kind Regards, \nThe Ember Table Team"
        )
    else:
        return

    send_mail(
        subject,
        message,
        "noreply@theembertable.com",
        [booking.customer.email],
        fail_silently=False,
    )
