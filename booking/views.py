from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Booking, Customer
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

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse(
                    {'reference_code': str(booking.reference_code)}
                    )

            return redirect(
                'booking:success', reference_code=booking.reference_code
                )
    else:
        form = MakeBookingForm()

    return render(request, 'include/make_booking_modal.html', {'form': form})


@login_required
def booking_cancelled(request):
    return render(request, 'include/booking_cancelled.html')


@login_required
def update_booking(request):
    """
    Handles updating a booking's date, time, or party size for a logged-in
    member.
    """
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        messages.error(request, "Customer not found")
        return redirect('user:members_info')

    if request.method == "POST":
        form = UpdateBookingForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['reference_code']
            try:
                booking = Booking.objects.get(
                    reference_code=code, customer=customer
                    )
                booking.date = form.cleaned_data.get('date', booking.date)
                booking.time = form.cleaned_data.get('time', booking.time)
                booking.party_size = form.cleaned_data.get(
                    'party_size', booking.party_size
                    )

                booking.save()
                messages.success(request, "Booking updated successfully")
                return redirect('user:members_dashboard')

            except Booking.DoesNotExist:
                form.add_error('reference_code', 'Invalid booking code')
    else:
        form = UpdateBookingForm()

    return render(request, 'user/member_dashbaord.html', {'form': form})


@login_required
def success(request, reference_code):
    return render(request, 'include/success_modal.html', {
        'reference_code': reference_code
    })
