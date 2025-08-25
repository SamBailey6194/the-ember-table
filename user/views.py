from django.contrib.auth import authenticate, login, logout
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
    Renders the members info page showing login and signup buttons.
    When clicked they load the signup and login modals.

    **Context**
    Provided globally by ``global_modal_urls``:
    - ``dashboard_url`` → The URL of :view:`user.members_dashboard`.
    - ``next_url`` → The `next` URL parameter if provided, otherwise the
        dashboard.

    **Template:**
    :template:`user/members_info.html`
    """
    return render(request, 'user/members_info.html')


def custom_signup(request):
    """
    Handles user signup from a modal form.

    Validates passwords and checks username availability.
    On success, creates a :model:`auth.User` and logs them in.
    Redirects to `next` if provided, otherwise to the dashboard.

    **Context**
    None (all handled internally)

    **Template:**
    Redirect only (no direct template rendering).
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

        login(request, user)
        return redirect(resolve_url(next_url))

    return redirect(reverse('user:members_info'))


def custom_login(request):
    """
    Handles user login from a modal form.

    Authenticates :model:`auth.User` with provided credentials.
    Redirects to `next` if provided, otherwise the dashboard.
    On failure, flashes error messages and redirects back.

    **Context**
    None (all handled internally)

    **Template:**
    Redirect only (no direct template rendering).
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
            return redirect(next_url)
        else:
            messages.error(request, "Invalid credentials")
            return redirect(next_url)

    return redirect(reverse('user:members_info'))


@login_required
def custom_logout(request):
    """
    A protected view for only those who are logged in.

    Logs out the current user.

    If `POST`, invalidates the session.
    Redirects to `next` if provided, otherwise home.

    **Context**
    None

    **Template:**
    Redirect only (no direct template rendering).
    """
    if request.method == 'POST':
        logout(request)
    return redirect('/')


@login_required
def members_dashboard(request):
    """
    A protected view for only those who are logged in.

    Displays the private dashboard for logged-in members.

    Shows all :model:`booking.Booking` objects for the logged-in
    :model:`booking.Customer`, excluding cancelled bookings.
    Provides :form:`booking.CancelBookingForm` and
    :form:`booking.UpdateBookingForm` for inline actions.

    **Context**
    ``bookings``
        A queryset of the user’s active bookings.
    ``cancel_form``
        An instance of :form:`booking.CancelBookingForm`.
    ``update_form``
        An instance of :form:`booking.UpdateBookingForm`.

    **Template:**
    :template:`user/members_dashboard.html`
    """
    try:
        customer = Customer.objects.get(user=request.user)
        bookings = Booking.objects.filter(
            customer=customer,
            status__in=['pending', 'confirmed', 'unavailable']
        ).order_by(
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
