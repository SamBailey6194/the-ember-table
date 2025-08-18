from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_time
from django.contrib.auth.decorators import login_required
from .models import Booking, Table, Customer


# Create your views here.

def booking_page(request):
    context = {
        'booking_page_url': reverse('booking:booking_page')
    }
    return render(request, 'booking/booking_page.html', context)


@login_required
def search_slots(request):
    available_slots = []
    message = ""
    if request.method == 'POST':
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guests = int(request.POST.get('guests', 1))

        booking_date = parse_date(date_str)
        booking_time = parse_time(time_str)

        if booking_date and booking_time:
            suitable_tables = Table.objects.filter(capacity__gte=guests)

            booked_tables = Booking.objects.filter(
                date=booking_date,
                time=booking_time,
                status__in=['pending', 'confirmed']
            ).values_list('table_id', flat=True)

            available_slots = suitable_tables.exclude(id__in=booked_tables)

            if available_slots:
                message = f"{available_slots.count()} table(s) available!"
            else:
                message = "No tables available for this time."
        else:
            message = "Invalid date or time."

    return render(request, 'booking/search_slots.html', {
        'available_slots': available_slots,
        'message': message
    })


@login_required
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


@login_required
def booking_cancelled(request):
    return render(request, 'booking/booking_cancelled.html')


@login_required
def success(request):
    return render(request, 'booking/success.html')
