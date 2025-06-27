from django.test import TestCase
from django.contrib.auth.models import User
from booking.models import Menu


class AdminMenuTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        self.client.login(username='admin', password='adminpass')
        self.menu = Menu.objects.create(
            name="Summer Specials",
            is_active=True,
            start_date="2025-06-01",
            end_date="2025-09-01",
        )

    def test_admin_can_toggle_menu_activation(self):
        response = self.client.post(
            f'/admin/booking/menu/{self.menu.id}/change/',
            {
                'name': self.menu.name,
                'is_active': False,
                'start_date': self.menu.start_date,
                'end_date': self.menu.end_date,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.menu.refresh_from_db()
        self.assertFalse(self.menu.is_active)
