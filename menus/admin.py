from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Menu, MenuItem


# Register your models here.
class MenuItemInLine(admin.TabularInline):
    """
    Allows inline editing of MenuItems within a Menu
    """
    model = MenuItem
    extra = 1
    fields = ('name', 'ingredients', 'description', 'price', 'is_available')
    show_change_link = True


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Menus
    """
    list_display = (
        'name', 'is_active', 'start_date', 'end_date', 'auto_renew_yearly'
        )
    list_filter = ('is_active', 'auto_renew_yearly')
    search_fields = ('name')
    inlines = [MenuItemInLine]


@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    """
    Admin interface for MenuItems using Summernote for descriptions
    """
    list_display = ('name', 'menu', 'price', 'is_available')
    list_filter = ('menu', 'is_available')
    search_fields = ('name', 'ingredients')
    summernote_fields = ('description')
