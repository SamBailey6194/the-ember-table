from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from booking.models import Customer


class UserViewsTest(TestCase):
    def setUp(self):
        # Create a test user and customer
        self.password = "TestPass123"
        self.user = User.objects.create_user(
            username="testuser",
            password=self.password,
            first_name="Test",
            last_name="User",
            email="test@example.com"
        )
        self.customer = Customer.objects.create(
            user=self.user,
            customer_fname="Test",
            customer_lname="User",
            email="test@example.com",
            phone="1234567890"
        )

    def test_members_info_view(self):
        url = reverse("user:members_info")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/members_info.html")

    def test_custom_signup_success(self):
        url = reverse("user:custom_signup")
        response = self.client.post(url, {
            "username": "newuser",
            "customer_fname": "New",
            "customer_lname": "User",
            "email": "new@example.com",
            "phone": "1111111111",
            "password1": "NewPass123",
            "password2": "NewPass123",
        }, follow=True)

        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertTrue(
            Customer.objects.filter(user__username="newuser").exists()
            )
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Welcome newuser!", messages[0])

    def test_custom_signup_password_mismatch(self):
        url = reverse("user:custom_signup")
        response = self.client.post(url, {
            "username": "baduser",
            "password1": "12345",
            "password2": "54321",
        }, follow=True)
        self.assertFalse(User.objects.filter(username="baduser").exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Passwords do not match", messages)

    def test_custom_signup_existing_username(self):
        url = reverse("user:custom_signup")
        response = self.client.post(url, {
            "username": "testuser",  # Already exists
            "password1": "TestPass123",
            "password2": "TestPass123",
        }, follow=True)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Username already exists", messages)

    def test_custom_login_success(self):
        url = reverse("user:custom_login")
        response = self.client.post(url, {
            "login": "testuser",
            "password": self.password
        }, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Welcome back testuser!", messages[0])

    def test_custom_login_invalid_credentials(self):
        url = reverse("user:custom_login")
        response = self.client.post(url, {
            "login": "testuser",
            "password": "WrongPass"
        }, follow=True)
        self.assertFalse(response.context["user"].is_authenticated)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Invalid credentials", messages[0])

    def test_custom_logout(self):
        self.client.login(username="testuser", password=self.password)
        url = reverse("user:custom_logout")
        response = self.client.post(url, follow=True)
        self.assertFalse(response.context["user"].is_authenticated)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("You have successfully logged out.", messages)

    def test_members_dashboard_authenticated(self):
        self.client.login(username="testuser", password=self.password)
        url = reverse("user:members_dashboard")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/members_dashboard.html")
        self.assertIn("bookings", response.context)
        self.assertIn("cancel_form", response.context)
        self.assertIn("update_form", response.context)

    def test_members_dashboard_no_customer(self):
        User.objects.create_user(
            username="nocustomer", password="pass123"
            )
        self.client.login(username="nocustomer", password="pass123")
        url = reverse("user:members_dashboard")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["bookings"]), [])
