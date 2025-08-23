from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
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
    return render(request, 'include/booking_cancelled_modal.html')


@login_required
@require_POST
def cancel_booking(request):
    reference_code = request.POST.get('reference_code')
    try:
        booking = Booking.objects.get(
            reference_code=reference_code,
            customer=request.user.customer
        )
        booking.status = 'cancelled'
        booking.save()

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "success": True,
                "reference_code": reference_code,
                "status": booking.get_status_display(),
            })

        messages.success(request, "Booking cancelled successfully")
    except Booking.DoesNotExist:
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse(
                {"success": False, "error": "Invalid booking reference"},
                status=404
            )
        messages.error(request, "Invalid booking reference")

    return redirect('user:members_dashboard')


@login_required
def update_booking(request, booking_id):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)

    try:
        booking = Booking.objects.get(id=booking_id, customer=customer)
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)

    if request.method == "POST":
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {'success': True, 'reference_code': booking.reference_code}
            )
        else:
            return JsonResponse(
                {'error': 'Invalid form data', 'errors': form.errors},
                status=400
            )
    else:
        form = UpdateBookingForm(instance=booking)
        return render(request, "include/booking_update_modal.html", {
            "form": form, "booking": booking
            })


@login_required
def success(request, reference_code):
    return render(request, 'include/success_modal.html', {
        'reference_code': reference_code
    })
