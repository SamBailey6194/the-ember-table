from django.test import TestCase
from booking.models import Customer, Table, Booking
from django.contrib.auth.models import User
from datetime import date, time, timedelta


class ModelTests(TestCase):
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
        self.table = Table.objects.create(number=1, capacity=4)
        self.booking = Booking.objects.create(
            customer=self.customer,
            date=date.today() + timedelta(days=1),
            time=time(12, 30),
            party_size=2,
            table=self.table
        )

    def test_customer_str(self):
        self.assertEqual(str(self.customer), self.user.username)

    def test_table_str(self):
        self.assertEqual(str(self.table), "Table 1 (Capacity: 4)")

    def test_booking_str(self):
        self.assertIn("Booking", str(self.booking))
        self.assertIn(str(self.booking.reference_code), str(self.booking))
