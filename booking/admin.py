from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Booking, BookingManagement, Table, TableAssignment, Customer
    )


# Register your models here.
class CustomUserAdmin(UserAdmin):
    """
    Creating custom fields to be able to create staff users with all
    relevant information
    """
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
            )
        }),
    )


@admin.register(BookingManagement)
class BookingManagementAdmin(SummernoteModelAdmin):
    """
    Adds relevant fields to summernote BookingManagement for admins
    """
    summernote_fields = ('notes',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Booking)
admin.site.register(Table)
admin.site.register(TableAssignment)
admin.site.register(Customer)
