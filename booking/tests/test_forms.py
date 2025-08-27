from django.test import TestCase
from datetime import date, time, timedelta
from booking.forms import MakeBookingForm, CancelBookingForm, UpdateBookingForm
from booking.models import Booking, Customer
from django.contrib.auth.models import User
import uuid


class MakeBookingFormTest(TestCase):
    def test_valid_form(self):
        form = MakeBookingForm(data={
            'date': date.today() + timedelta(days=1),
            'time': time(12, 30),
            'party_size': 4
        })
        self.assertTrue(form.is_valid())

    def test_invalid_party_size(self):
        form = MakeBookingForm(data={
            'date': date.today() + timedelta(days=1),
            'time': time(12, 30),
            'party_size': 25
        })
        self.assertFalse(form.is_valid())
        self.assertIn('party_size', form.errors)

    def test_invalid_past_date(self):
        form = MakeBookingForm(data={
            'date': date.today() - timedelta(days=1),
            'time': time(12, 30),
            'party_size': 2
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_invalid_time(self):
        form = MakeBookingForm(data={
            'date': date.today() + timedelta(days=1),
            'time': time(9, 0),  # too early
            'party_size': 2
        })
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors)


class CancelBookingFormTest(TestCase):
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

    def test_valid_reference_code(self):
        form = CancelBookingForm(
            data={'reference_code': str(self.booking.reference_code)}
            )
        self.assertTrue(form.is_valid())

    def test_invalid_reference_code(self):
        form = CancelBookingForm(data={'reference_code': str(uuid.uuid4())})
        self.assertFalse(form.is_valid())
        self.assertIn('reference_code', form.errors)


class UpdateBookingFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester2", password="pass123"
            )
        self.customer = Customer.objects.create(
            user=self.user,
            phone="07123456780",
            email="test2@example.com",
            customer_fname="Foo",
            customer_lname="Bar",
        )
        self.booking = Booking.objects.create(
            customer=self.customer,
            date=date.today() + timedelta(days=1),
            time=time(15, 0),
            party_size=3,
        )

    def test_valid_update(self):
        form = UpdateBookingForm(
            data={
                'reference_code': str(self.booking.reference_code),
                'date': date.today() + timedelta(days=2),
                'time': time(16, 0),
                'party_size': 4
            },
            instance=self.booking
        )
        self.assertTrue(form.is_valid())

    def test_invalid_reference_code(self):
        form = UpdateBookingForm(
            data={
                'reference_code': str(uuid.uuid4()),
                'date': date.today() + timedelta(days=2),
                'time': time(16, 0),
                'party_size': 4
            },
            instance=self.booking
        )
        self.assertFalse(form.is_valid())
        self.assertIn('reference_code', form.errors)
