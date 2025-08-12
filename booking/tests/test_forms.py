from django.test import TestCase
from datetime import date, timedelta
from ..forms import SearchSlotsForm, MakeBookingForm, CancelBookingForm
from . import helpers


class BookingTestSetUp(TestCase):
    """
    Base test setup for booking form tests.
    """
    def setUp(self):
        self.reg_customer = helpers.create_fake_registered_customer()
        self.guest_customer = helpers.create_fake_guest_customer()
        self.table = helpers.create_fake_table()
        self.booking = helpers.create_fake_booking(
            customer=self.reg_customer, table=self.table
            )


class SearchSlotsFormTests(BookingTestSetUp):
    """
    Tests for SearchSlotsForm validation.
    """

    def test_valid_date(self):
        form = SearchSlotsForm(data={'date': '2025-08-20'})
        self.assertTrue(form.is_valid())

    def test_invalid_date_format(self):
        form = SearchSlotsForm(data={'date': '20/08/2025'})
        self.assertFalse(form.is_valid())
        self.assertIn('Invalid date format', str(form.errors))


class MakeBookingFormTests(BookingTestSetUp):
    """
    Tests for MakeBookingForm validation.
    """

    def test_valid_form(self):
        form_data = {
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time': '18:00',
            'party_size': 2,
            'tables': [self.table.id],
            'contact_name': 'John Doe',
            'contact_email': 'john@example.com',
            'contact_phone': '0123456789',
        }
        form = MakeBookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_party_sizes(self):
        for size in [0, -1, 1000]:
            with self.subTest(party_size=size):
                form_data = {
                    'date': (
                        date.today() + timedelta(days=1)
                        ).strftime('%Y-%m-%d'),
                    'time': '18:00',
                    'party_size': size,
                    'tables': [self.table.id],
                    'contact_name': 'John Doe',
                    'contact_email': 'john@example.com',
                    'contact_phone': '0123456789',
                }
                form = MakeBookingForm(data=form_data)
                self.assertFalse(form.is_valid())
                self.assertIn('party_size', form.errors)

    def test_invalid_email_format(self):
        form_data = {
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time': '18:00',
            'party_size': 2,
            'tables': [self.table.id],
            'contact_name': 'John Doe',
            'contact_email': 'invalid-email',
            'contact_phone': '0123456789',
        }
        form = MakeBookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('contact_email', form.errors)
        self.assertIn(
            'Enter a valid email address', form.errors['contact_email'][0]
            )

    def test_missing_required_fields(self):
        required_fields = [
            'date',
            'time',
            'party_size',
            'tables',
            'contact_name',
            'contact_email',
            'contact_phone'
            ]
        for field in required_fields:
            with self.subTest(missing_field=field):
                form_data = {
                    'date': (
                        date.today() + timedelta(days=1)
                        ).strftime('%Y-%m-%d'),
                    'time': '18:00',
                    'party_size': 2,
                    'tables': [self.table.id],
                    'contact_name': 'John Doe',
                    'contact_email': 'john@example.com',
                    'contact_phone': '0123456789',
                }
                form_data.pop(field)
                form = MakeBookingForm(data=form_data)
                self.assertFalse(form.is_valid())
                self.assertIn(field, form.errors)
                self.assertIn('This field is required', form.errors[field][0])


class CancelBookingFormTests(BookingTestSetUp):
    """
    Tests for CancelBookingForm validation.
    """

    def test_valid_reference_code(self):
        form = CancelBookingForm(
            data={'reference_code': self.booking.reference_code}
            )
        self.assertTrue(form.is_valid())

    def test_invalid_reference_code(self):
        form = CancelBookingForm(data={'reference_code': 'NONEXISTENT'})
        self.assertFalse(form.is_valid())
        self.assertIn('reference_code', form.errors)
        self.assertIn(
            'Invalid reference code', str(form.errors['reference_code'])
            )
