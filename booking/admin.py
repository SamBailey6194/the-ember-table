from django.contrib import admin
from .models import Booking, Customer, Table


# Register your models here
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone', 'is_guest']


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
        'reference_code', 'customer__username__username', 'customer__email'
        ]
