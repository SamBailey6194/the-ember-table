from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Booking


# Create your views here.
def home(request):
    return render(request, 'booking/home.html')


class BookingCreateView(CreateView):
    """
    Display an individual :model:`booking.Booking`.

    **Context**

    ``booking``
        An instance of :model:`booking.Booking`

    **Template:**

    :template: booking/booking_form.html
    """
    model = Booking
    fields = ['customer', 'party_size', 'date', 'time']
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking-thanks')
