from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Booking
from .forms import MakeBookingForm, UpdateBookingForm


# Create your views here.
def booking_page(request):
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
    if request.method == 'POST':
        form = MakeBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user.customer
            booking.save()
            messages.success(
                request,
                f"Booking {booking.reference_code} created successfully"
                )
            return redirect('booking:booking_page')
        else:
            messages.error(request, "Invalid booking data")
            return redirect('booking:booking_page')
    else:
        form = MakeBookingForm()

    return render(request, 'include/make_booking_modal.html', {'form': form})


@login_required
def booking_cancelled(request):
    return render(request, 'include/booking_cancelled_modal.html')


@login_required
@require_POST
def cancel_booking(request):
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


@login_required
def success(request, reference_code):
    return render(request, 'include/success_modal.html', {
        'reference_code': reference_code
    })
