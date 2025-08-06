from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from ..models import Booking, Table


class SearchBookingSlotsTests(TestCase):
    def setUp(self):
        self.table = Table.objects.create(name="Table 1", seats=4)

    def test_get_available_slots(self):
        response = self.client.get(reverse("booking:search_slots"), {
            "date": date.today().strftime('%d-%m-%Y'),
            "guests": 2
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('available_slots', response.context)


class MakeBookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='pass'
            )
        self.table = Table.objects.create(name="Table 1", seats=4)
        self.client.login(username="testuser", password="pass")

    def test_make_booking(self):
        response = self.client.post(reverse("booking:make_booking"), {
            'date': '10-08-2025',
            'time': '19:00',
            'guests': 2,
            'table_id': self.table.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.table, self.table)


class CancelBookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='pass'
            )
        self.table = Table.objects.create(name="Table 1", seats=4)
        self.booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date='2025-08-10',
            time='19:00',
            guests=2,
            status='confirmed'
        )
        self.client.login(username='testuser', password='pass')

    def test_cancel_booking(self):
        response = self.client.post(reverse(
            'booking:cancel_booking', args=[self.booking.id]
            ))
        self.assertEqual(response.status_code, 302)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'cancelled')
