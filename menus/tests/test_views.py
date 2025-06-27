from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from ..models import Menu, MenuItem


class MenuViewTests(TestCase):
    def setUp(self):
        self.standard_menu = Menu.objects.create(
            name="Menu",
            is_active=True,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=365),
        )
        self.seasonal_menu = Menu.objects.create(
            name="Summer Specials",
            is_active=True,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=90),
        )
        MenuItem.objects.create(
            menu=self.standard_menu,
            name="Ember Table Burger",
            ingredients="Bun, Beef Burger, Lettuce, Tomato, Onion",
            price=9.99,
            is_available=True,
        )
        MenuItem.objects.create(
            menu=self.seasonal_menu,
            name="Grilled Salmon",
            ingredients="Salmon, Lemon, Herbs",
            price=15.99,
            is_available=True,
        )

    def test_menu_page_shows_active_menus(self):
        response = self.client.get(reverse('menu-list'))
        self.assertContains(response, "Menu")
        self.assertContains(response, "Summer Specials")

    def test_menu_page_excludes_inactive(self):
        inactive_menu = Menu.objects.create(
            name="Christmas Season",
            is_active=False,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=60),
        )
        response = self.client.get(reverse('menu-list'))
        self.assertNotContains(response, inactive_menu.name)
