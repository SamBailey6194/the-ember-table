from django.core.mail import send_email


def send_status_email(booking):
    """
    Send email to the customer based on booking status
    """
    subject = None
    message = None

    if booking.status == "pending":
        subject = "Booking Pending"
        message = (
            f"Dear {booking.customer.customer_fname},\n\n"
            "Thank you for sending a booking request to The Ember Table! "
            f"We will seek to confirm your booking asap for {booking.date} at "
            f"{booking.time}.\n\n"
            "Kind Regards, \nThe Ember Table Team"
        )
    elif booking.status == "confirmed":
        subject = "Booking Confirmed"
        message = (
            f"Dear {booking.customer.customer_fname},\n\n"
            "Thank you for booking with The Ember Table! "
            f"Your reservation on {booking.date} at {booking.time} "
            "has been confirmed.\n\n"
            "We look forward to welcoming you!"
            "Kind Regards, \nThe Ember Table Team"
        )
    elif booking.status == "unavailable":
        subject = "Booking Unavailable"
        message = (
            f"Dear {booking.customer.customer_fname},\n\n"
            "We regret to inform you that your requested booking "
            f"for {booking.date} at {booking.time} is unavailable.\n"
            "We apologise for any convenience caused.\n\n"
            "Please fill out the form again to find another suitable time.\n"
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
