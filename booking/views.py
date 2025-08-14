from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_date
from .forms import CancelBookingForm
from .models import Booking, Table, Customer


# Create your views here.
def booking_page(request):
    return render(request, 'booking/booking.html')


def search_slots(request):
    available_slots = []

    return render(
        request, 'booking/search_slots.html', {
            'available_slots': available_slots
            }
        )


def make_booking(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guests = int(request.POST.get('guests', 1))
        table_id = request.POST.get('table_id')

        if not all([date_str, time_str, guests, table_id]):
            messages.error(request, "Please fill all fields.")
            return redirect('booking:make_booking')

        booking_date = parse_date(date_str)
        if not booking_date:
            messages.error(request, "Invalid date format.")
            return redirect('booking:make_booking')

        try:
            table = Table.objects.get(pk=table_id)
        except Table.DoesNotExist:
            messages.error(request, "Table not found.")
            return redirect('booking:make_booking')

        customer = None
        if request.user.is_authenticated:
            try:
                customer = request.user.customer
            except Customer.DoesNotExist:
                customer = None

        Booking.objects.create(
            date=booking_date,
            time=time_str,
            party_size=guests,
            table=table,
            customer=customer,
            status='pending'
        )

        messages.success(request, "Booking created successfully!")
        return redirect('/')

    return render(request, 'booking/make_booking.html', {})


def manage_booking(request):
    if request.method == 'POST':
        form = CancelBookingForm(request.POST)
        if form.is_valid():
            booking = Booking.objects.get(
                reference_code=form.cleaned_data['reference_code']
                )
            booking.status = 'cancelled'
            booking.save()
            messages.success(request, 'Your booking has been cancelled.')
            return redirect('booking:booking_cancelled')
    else:
        form = CancelBookingForm()
    return render(request, 'booking/manage_booking.html', {'form': form})


def booking_cancelled(request):
    return render(request, 'booking/booking_cancelled.html')


def success(request):
    return render(request, 'booking/success.html')
