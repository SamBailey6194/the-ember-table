from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Booking, Table, BookingManagement


# Create your views here.
def is_staff_user(user):
    """
    Checks user is a staff user
    """
    return user.is_staff


class BookingCreativeView(CreateView):
    model = Booking
