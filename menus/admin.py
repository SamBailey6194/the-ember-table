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


@admin.action(description="Renew selected menus for next year")
def renew_menus_for_next_year(modeladmin, request, queryset):
    """
    Provides admin with button to renew the menus that are
    auto_renew_yearly=True
    """
    renewed_menus = []
    for menu in queryset:
        new_menu = menu.renew_for_next_year()
        if new_menu:
            renewed_menus.append(new_menu.name)
    if renewed_menus:
        modeladmin.message_user(
            request,
            f"Successfully renewed menus: {', '.join(renewed_menus)}"
        )
    else:
        modeladmin.message_user(request, "No menus needed renewal.")


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Menus
    """
    list_display = (
        'name', 'is_active', 'start_date', 'end_date', 'auto_renew_yearly'
        )
    list_filter = ('is_active', 'auto_renew_yearly')
    search_fields = ("name", "name")
    inlines = [MenuItemInLine]
    actions = [renew_menus_for_next_year]


@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    """
    Admin interface for MenuItems using Summernote for descriptions
    """
    list_display = ('name', 'menu', 'price', 'is_available')
    list_filter = ('menu', 'is_available')
    search_fields = (
        ('name', "name"),
        ('ingredients', "ingredients"),
        )
    summernote_fields = ('description')
