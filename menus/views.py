from django.shortcuts import render, get_object_or_404
from .models import Menu


# Create your views here.
def public_menu_list(request):
    """
    Display a list of active :model:`menus.Menu`.

    **Context**

    ``menu_list``
        A list of currently active menus.

    **Template:**

    :template:`menus/menu_list.html`
    """
    menus = Menu.objects.filter(is_active=True)
    active_menus = [menu for menu in menus if menu.is_currently_active()]
    return render(request, 'menus/menu_list.html', {
        'menus': active_menus
    })


def menu_detail(request, menu_id):
    """
    Display a individual menus with items :model:`menus.MenuItems`.

    **Context**

    ``menu_shown``
        A list of items on a specific menu.

    **Template:**

    :template:`menus/menu_display.html`
    """
    menu = get_object_or_404(Menu, id=menu_id, is_active=True)
    return render(request, 'menus/menu_display.html', {'menu': menu})
