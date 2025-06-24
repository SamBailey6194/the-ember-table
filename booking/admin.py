from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


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


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
