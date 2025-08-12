from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
from ..utils import send_status_email
from . import helpers


class BookingTestSetUp(TestCase):
    """
    Base test setup to create common test data for bookings,
    including an admin user.
    """
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin",
            password="password123",
            email="admin@example.com"
        )
        self.client.login(username="admin", password="password123")

        self.customer = helpers.create_fake_registered_customer()
        self.user = self.customer.username
        self.guest_customer = helpers.create_fake_guest_customer()
        self.table = helpers.create_fake_table()
        self.booking = helpers.create_fake_booking()


class AdminBookingActionsTest(BookingTestSetUp):
    """
    Test suite for admin-related booking actions.
    """

    def test_admin_can_login(self):
        """Admin user should be able to log in successfully."""
        login_successful = self.client.login(
            username="admin",
            password="password123"
        )
        self.assertTrue(login_successful)

    def test_email_sent_when_booking_status_is_pending(self):
        """Ensure an email is sent when booking status is 'pending'."""
        mail.outbox = []

        send_status_email(self.booking)

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        expected_subject = f"Booking Pending - Ref: {
            self.booking.reference_code
            }"
        expected_first_name = (
            self.booking.customer.username.first_name
            if self.booking.customer.username
            else self.booking.customer.customer_fname
        )

        self.assertEqual(email.subject, expected_subject)
        self.assertIn(expected_first_name, email.body)
        self.assertIn(str(self.booking.date), email.body)
        self.assertIn(str(self.booking.time), email.body)
        self.assertIn(self.booking.reference_code, email.body)
        self.assertIn(self.booking.customer.email, email.to)

    def test_admin_can_update_booking_status(self):
        """
        Test that updating booking status triggers correct email notifications,
        according to the transition.
        """
        transitions = [
            ("pending", "confirmed", True, "Booking confirmation"),
            ("pending", "unavailable", True, "Booking Unavailable"),
            ("confirmed", "cancelled", True, "Booking Cancelled"),
            ("confirmed", "seated", False, None),
        ]

        for (
            initial_status,
            new_status,
            email_expected,
            expected_subject
        ) in transitions:
            with self.subTest(
                initial_status=initial_status, new_status=new_status
            ):
                self.booking.status = initial_status
                self.booking.save()
                mail.outbox = []

                self.booking.status = new_status
                self.booking.save()

                send_status_email(self.booking)

                self.booking.refresh_from_db()
                self.assertEqual(self.booking.status, new_status)

                if email_expected:
                    self.assertEqual(len(mail.outbox), 1)
                    self.assertIn(expected_subject, mail.outbox[0].subject)
                    self.assertIn(
                        self.booking.customer.email, mail.outbox[0].to
                        )
                else:
                    self.assertEqual(len(mail.outbox), 0)

    def test_invalid_status_update_sends_no_email(self):
        """
        If booking status is updated to an unknown status,
        no email should be sent.
        """
        self.booking.status = "pending"
        self.booking.save()
        mail.outbox = []

        self.booking.status = "invalid_status"
        self.booking.save()

        send_status_email(self.booking)

        self.assertEqual(len(mail.outbox), 0)

    def test_admin_can_assign_table_to_booking(self):
        """Admin can assign a table to a booking."""
        self.booking.table = self.table
        self.booking.save()
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.table, self.table)
