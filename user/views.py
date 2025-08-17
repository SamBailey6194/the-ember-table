from django.contrib.auth import authenticate, login, get_backends
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from booking.models import Customer, Booking
from booking.forms import CancelBookingForm


def members_info(request):
    """Public members info page"""
    return render(request, 'user/members_info.html')


def custom_signup(request):
    """Handle signup from modal with validation"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('user:members_info')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('user:members_info')

        user = User.objects.create_user(
            username=username, email=email, password=password1
            )

        backend = get_backends()[0]
        login(
            request, user, backend=(
                f"{backend.__module__}.{backend.__class__.__name__}"
                )
            )
        return redirect('user:members_dashboard')

    return redirect('user:members_info')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('user:members_dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return redirect('user:members_info')


@login_required
def members_dashboard(request):
    """Private dashboard for logged-in members with booking cancellation"""
    try:
        customer = Customer.objects.get(username=request.user)
        bookings = Booking.objects.filter(customer=customer)
    except Customer.DoesNotExist:
        bookings = []

    cancel_form = CancelBookingForm(request.POST or None)

    if request.method == 'POST' and cancel_form.is_valid():
        code = cancel_form.cleaned_data['reference_code']
        try:
            booking = Booking.objects.get(
                reference_code=code, customer=customer
                )
            booking.status = 'cancelled'
            booking.save()
        except Booking.DoesNotExist:
            cancel_form.add_error('reference_code', 'Invalid booking code.')
        return redirect('user:members_dashboard')

    return render(request, 'user/members_dashboard.html', {
        'bookings': bookings,
        'cancel_form': cancel_form,
    })
