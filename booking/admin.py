from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Booking, BookingManagement, Table, TableAssignment, Customer
    )


# Register your models here.
