from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Customer, Booking
from booking.forms import CancelBookingForm


# Create your views here.
def members_info(request):
    """Public members info page"""
    return render(request, 'user/members_info.html')


@login_required
def members_dashboard(request):
    """Private dashboard for logged-in members with booking cancellation"""
    try:
        customer = Customer.objects.get(username=request.user)
        bookings = Booking.objects.filter(customer=customer)
    except Customer.DoesNotExist:
        bookings = []

    cancel_form = CancelBookingForm()

    if request.method == 'POST':
        cancel_form = CancelBookingForm(request.POST)
        if cancel_form.is_valid():
            code = cancel_form.cleaned_data['reference_code']
            booking = Booking.objects.get(reference_code=code)
            booking.status = 'cancelled'
            booking.save()
            return redirect('user:members_dashboard')

    return render(request, 'user/members_dashboard.html', {
        'bookings': bookings,
        'cancel_form': cancel_form,
    })



@login_required
def user_profile(request):
    """Optional: user profile page"""
    return render(request, 'user/profile.html', {'user': request.user})
