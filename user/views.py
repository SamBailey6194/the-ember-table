from django.contrib.auth import authenticate, login, logout, get_backends
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from booking.models import Customer, Booking
from booking.forms import CancelBookingForm, UpdateBookingForm
from django.shortcuts import resolve_url


def members_info(request):
    """
    Page showing member info with login/signup modals.
    """
    context = {
        'dashboard_url': reverse('user:members_dashboard'),
        'next_url': request.GET.get('next', request.path)
    }
    return render(request, 'user/members_info.html', context)


def custom_signup(request):
    """
    Handle signup from modal with validation.
    Redirects to 'next' if provided, otherwise dashboard.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        next_url = request.POST.get('next') or reverse(
            'user:members_dashboard'
            )

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect(resolve_url(next_url))

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect(resolve_url(next_url))

        user = User.objects.create_user(
            username=username, email=email, password=password1
            )

        backend = get_backends()[0]
        login(
            request, user, backend=f"{backend.__module__}.{
                backend.__class__.__name__
                }"
            )

        return redirect(resolve_url(next_url))

    return redirect(
        resolve_url(request.POST.get('next') or reverse('user:members_info'))
        )


def custom_login(request):
    """
    Handle login from modal.
    Redirects to 'next' if provided, otherwise dashboard.
    """
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        next_url = request.POST.get('next') or reverse(
            'user:members_dashboard'
            )

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(resolve_url(next_url))
        else:
            messages.error(request, "Invalid credentials")
            return redirect(resolve_url(next_url))

    return redirect(reverse('user:members_info'))


@login_required
def custom_logout(request):
    """
    Logs out the user.
    Redirects to 'next' if provided, otherwise home page.
    """
    if request.method == 'POST':
        logout(request)
    return redirect('/')


@login_required
def members_dashboard(request):
    """
    Private dashboard for logged-in members showing all bookings.
    Any update or cancellation is handled in their respective views,
    with messages displayed on redirect.
    """
    try:
        customer = Customer.objects.get(user=request.user)
        bookings = Booking.objects.filter(customer=customer).order_by(
            'date', 'time'
            )
    except Customer.DoesNotExist:
        bookings = []

    cancel_form = CancelBookingForm()
    update_form = UpdateBookingForm()

    return render(request, 'user/members_dashboard.html', {
        'bookings': bookings,
        'cancel_form': cancel_form,
        'update_form': update_form,
    })
