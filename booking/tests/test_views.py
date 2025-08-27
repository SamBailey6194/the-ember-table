from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from booking.models import Customer, Booking
from datetime import date, time, timedelta


class BookingViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester", password="pass123"
            )
        self.customer = Customer.objects.create(
            user=self.user,
            phone="07123456789",
            email="test@example.com",
            customer_fname="Test",
            customer_lname="User",
        )
        self.booking = Booking.objects.create(
            customer=self.customer,
            date=date.today() + timedelta(days=1),
            time=time(13, 0),
            party_size=2,
        )

    def test_booking_page_get(self):
        url = reverse('booking:booking_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_page.html')

    def test_make_booking_requires_login(self):
        url = reverse('booking:make_booking')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_make_booking_post_valid(self):
        self.client.login(username="tester", password="pass123")
        url = reverse('booking:make_booking')
        response = self.client.post(url, {
            'date': date.today() + timedelta(days=1),
            'time': time(12, 30),
            'party_size': 2,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:members_dashboard'))
        self.assertTrue(
            Booking.objects.filter(customer=self.customer).exists()
            )

    def test_cancel_booking_valid(self):
        self.client.login(username="tester", password="pass123")
        url = reverse('booking:cancel_booking')
        response = self.client.post(url, {
            'reference_code': str(self.booking.reference_code)
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:members_dashboard'))
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'cancelled')

    def test_cancel_booking_invalid(self):
        self.client.login(username="tester", password="pass123")
        url = reverse('booking:cancel_booking')
        response = self.client.post(
            url, {'reference_code': "00000000-0000-0000-0000-000000000000"}
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:members_dashboard'))

    def test_update_booking_valid(self):
        self.client.login(username="tester", password="pass123")
        url = reverse('booking:update', args=[self.booking.id])
        response = self.client.post(url, {
            'reference_code': str(self.booking.reference_code),
            'date': date.today() + timedelta(days=2),
            'time': time(18, 0),
            'party_size': 3,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:members_dashboard'))
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.party_size, 3)

    def test_update_booking_not_found(self):
        self.client.login(username="tester", password="pass123")
        url = reverse('booking:update', args=[999])
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:members_dashboard'))
