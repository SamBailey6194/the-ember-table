from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from ..models import Menu, MenuItem


# Create your tests here.
class MenuModelTests(TestCase):
    def setUp(self):
        self.standard_menu = Menu.objects.create(
            name="Menu",
            is_active=True,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=365),
            auto_renew_yearly=False,
        )
        self.seasonal_menu = Menu.objects.create(
            name="Summer Specials",
            is_active=True,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() - timedelta(days=1),
            auto_renew_yearly=True,
        )

    def test_menu_creation(self):
        self.assertEqual(self.standard_menu.name, "Menu")
        self.assertTrue(self.standard_menu.is_active)

    def test_auto_renew_creates_new_menu(self):
        new_menu = self.seasonal_menu.auto_renew_if_needed()
        self.assertIsNotNone(new_menu)
        self.assertEqual(
            new_menu.name, self.seasonal_menu.name + " (Next Year)"
            )
        self.assertEqual(
            new_menu.start_date,
            self.seasonal_menu.start_date.replace(
                year=self.seasonal_menu.start_date.year + 1
                )
        )
        self.assertEqual(
            new_menu.end_date,
            self.seasonal_menu.end_date.replace(
                year=self.seasonal_menu.end_date.year + 1
                )
        )

    def test_menu_item_creation(self):
        item = MenuItem.objects.create(
            menu=self.standard_menu,
            name="Ember Table Burger",
            description="Delicious burger",
            ingredients="Bun, Beef Burger, Lettuce, Tomato, Onion",
            price=9.99,
            is_available=True,
        )
        self.assertEqual(item.name, "Ember Table Burger")
        self.assertTrue(item.is_available)
        self.assertEqual(item.menu, self.standard_menu)
