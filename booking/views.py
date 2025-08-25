from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Booking
from .forms import MakeBookingForm, UpdateBookingForm


# Create your views here.
def booking_page(request):
    """
    Renders the public booking page with the booking form buttons.
    When the button is booked a booking form modal is opened up.

    If `POST`, initializes :form:`booking.MakeBookingForm` with submitted
    data for validation.
    If `GET`, provides a blank form.

    **Context**
    ``booking_page_url``
        The URL of :view:`booking.booking_page` for form submission.
    ``form``
        An instance of :form:`booking.MakeBookingForm`.

    **Template:**
    :template:`booking/booking_page.html`
    """
    if request.method == "POST":
        form = MakeBookingForm(request.POST)
    else:
        form = MakeBookingForm()

    context = {
        'booking_page_url': reverse('booking:booking_page'),
        'form': form,
    }
    return render(request, 'booking/booking_page.html', context)


@login_required
def make_booking(request):
    """
    A protected view for only those who are logged in.

    Handles the creation of a new booking.

    Validates :form:`booking.MakeBookingForm`,
    attaches the booking to the logged-in :model:`booking.Customer`,
    and saves it. On success, redirects with a success message.

    **Context**
    ``form``
        An instance of :form:`booking.MakeBookingForm` (for modal rendering).

    **Template:**
    :template:`include/make_booking_modal.html
    """
    if request.method == 'POST':
        form = MakeBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user.customer
            booking.save()
            messages.success(
                request,
                "Booking Successful!<br>"
                "<br>"
                f"Reference Code: {booking.reference_code}.<br>"
                "<br>"
                "Your booking has been sent to the restaurant.<br>"
                "They will confirm availability.<br>"
                "<br>"
                "You can manage your bookings on your dashboard."
            )
            return redirect('user:members_dashboard')
        else:
            messages.error(
                request,
                "Please ensure your date and time are future dates and "
                "times.<br>"
                "<br>"
                "We also only allow up to a maximum of 20 people for party "
                "size."
                )
            return redirect('booking:booking_page')
    else:
        form = MakeBookingForm()

    return render(request, 'includes/make_booking_modal.html', {'form': form})


@login_required
def booking_cancelled(request):
    """
    A protected view for only those who are logged in.

    Renders the cancellation confirmation modal.

    Displays a static template after a booking has been cancelled.

    **Context**
    None

    **Template:**
    :template:`include/booking_cancelled_modal.html`
    """
    return render(request, 'includes/booking_cancelled_modal.html')


@login_required
@require_POST
def cancel_booking(request):
    """
    A protected view for only those who are logged in.

    Cancels an existing booking for the logged-in user.

    Finds :model:`booking.Booking` using the submitted ``reference_code``.
    If valid, updates the status to "cancelled".
    Displays success or error messages accordingly.

    **Context**
    None

    **Template:**
    Redirect only (messages displayed on :view:`user.members_dashboard`).
    """
    reference_code = request.POST.get('reference_code')
    try:
        booking = Booking.objects.get(
            reference_code=reference_code, customer=request.user.customer
            )
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, "Booking cancelled successfully")
    except Booking.DoesNotExist:
        messages.error(request, "Invalid booking reference")

    return redirect('user:members_dashboard')


@login_required
def update_booking(request, booking_id):
    """
    A protected view for only those who are logged in.

    Updates an existing booking for the logged-in user.

    Retrieves :model:`booking.Booking` by ID.
    On `POST`, validates and updates the booking using
    :form:`booking.UpdateBookingForm`.
    Redirects back to dashboard with messages.

    **Context**
    None (redirects immediately after POST).

    **Template:**
    Redirect only (messages displayed on :view:`user.members_dashboard`).
    """
    try:
        booking = Booking.objects.get(
            id=booking_id, customer=request.user.customer
            )
    except Booking.DoesNotExist:
        messages.error(request, "Booking not found")
        return redirect('user:members_dashboard')

    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Booking {booking.reference_code} updated successfully"
                )
        else:
            messages.error(request, "Invalid data. Please check your input.")
        return redirect('user:members_dashboard')
    else:
        form = UpdateBookingForm(instance=booking)

    return redirect('user:members_dashboard')
