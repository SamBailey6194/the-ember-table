from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from ..utils import send_status_email
from ..models import Booking, Table, Customer


# Create your tests here.
class AdminBookingActionsTest(TestCase):
    """
    Testing all admin actions
    """
    def setUp(self):
        """
        Mock customer and booking for tests
        """
        self.admin = User.objects.create_superuser(
            username="admin", password="password123", email="admin@example.com"
        )
        self.customer = Customer.objects.create(
            is_guest=True,
            customer_fname="Test",
            customer_lname="Name",
            email="testuser@example.com",
            phone="0123456789"
        )
        self.booking = Booking.objects.create(
            customer=self.customer,
            date="2025-12-01",
            time="18:00",
            party_size=2,
            status="pending",
        )
        self.table = Table.objects.create(number=1, capacity=4)

    def test_admin_can_login(self):
        """
        Testing admin login credentials
        """
        login = self.client.login(username="admin", password="password123")
        self.assertTrue(login)

    def test_email_sent_for_pending_booking(self):
        """
        Test that an email is sent when a booking is created with status
        'pending'
        """
        mail.outbox = []  # Clear any previous emails

        send_status_email(self.booking)

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        expected_subject = (
            f"Booking Pending - Ref: {self.booking.reference_code}"
            )
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
        self.assertIn(self.customer.email, email.to)

    def test_admin_can_update_booking_status(self):
        """
        Testing admin can update booking status
        """
        transitions = [
            ("pending", "confirmed", True,
             "Booking confirmation"
             ),
            ("pending", "unavailable", True,
             "Booking Unavailable"
             ),
            ("confirmed", "cancelled", True,
             "Booking Cancelled"
             ),
            ("confirmed", "seated", True, None),
        ]

        for (
            initial_status,
            new_status,
            email_expected,
            expected_subject,
        ) in transitions:
            with self.subTest(
                initial_status=initial_status,
                new_status=new_status
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
                    self.assertIn(self.customer.email, mail.outbox[0].to)
                else:
                    self.assertEqual(len(mail.outbox), 0)

    def test_admin_can_assign_table_to_booking(self):
        self.booking.table = self.table
        self.booking.save()
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.table, self.table)
