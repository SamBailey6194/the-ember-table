from django.contrib import admin
from .models import Booking, Customer, Table


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'email', 'phone', 'customer_fname', 'customer_lname'
        ]
    search_fields = [
        'user__username', 'customer_fname', 'customer_lname', 'email'
        ]


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'capacity']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'reference_code',
        'customer',
        'date',
        'time',
        'party_size',
        'status',
        'table'
    ]
    list_filter = ['status', 'date']
    search_fields = [
        'reference_code', 'customer__user__username', 'customer__email'
        ]
