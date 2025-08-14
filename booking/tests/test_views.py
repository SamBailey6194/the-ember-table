from django.test import TestCase
from django.urls import reverse
from datetime import date
from ..models import Booking, Customer, Table
from . import helpers


class BookingTestSetUp(TestCase):
    def setUp(self):
        Booking.objects.all().delete()
        Customer.objects.all().delete()
        Table.objects.all().delete()

        self.reg_customer = helpers.create_fake_registered_customer()
        self.guest_customer = helpers.create_fake_guest_customer()
        self.table = helpers.create_fake_table()


class SearchBookingSlotsTests(BookingTestSetUp):
    def test_get_available_slots(self):
        response = self.client.get(reverse("booking:search_slots"), {
            "date": date.today().strftime('%d-%m-%Y'),
            "guests": 2
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('available_slots', response.context)


class MakeBookingTests(BookingTestSetUp):
    def setUp(self):
        super().setUp()
        self.client.login(
            username=self.reg_customer.username.username, password='pass'
            )

    def test_make_booking(self):
        initial_count = Booking.objects.count()
        response = self.client.post(reverse("booking:make_booking"), {
            'date': '2025-08-10',
            'time': '19:00',
            'guests': 2,
            'table_id': self.table.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), initial_count + 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.customer, self.reg_customer)
        self.assertEqual(booking.table, self.table)

    def test_make_booking_unauthenticated(self):
        self.client.logout()
        response = self.client.post(reverse("booking:make_booking"), {
            'date': '10-08-2025',
            'time': '19:00',
            'guests': 2,
            'table_id': self.table.id
        })
        self.assertNotEqual(response.status_code, 200)


class CancelBookingTests(BookingTestSetUp):
    def setUp(self):
        super().setUp()
        self.booking = helpers.create_fake_booking()
        self.reg_booking = helpers.create_fake_registered_booking()
        self.guest_booking = helpers.create_fake_guest_booking()
        self.client.login(
            username=self.reg_customer.username.username, password='pass'
            )

    def test_cancel_booking(self):
        response = self.client.post(
            reverse('booking:manage_booking'),
            data={'reference_code': str(self.booking.reference_code)}
            )
        self.assertEqual(response.status_code, 302)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'cancelled')
