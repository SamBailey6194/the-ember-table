from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail


# Create your tests here.
class UserAccountTests(TestCase):
    """
    Test suite for user account features including registration, login,
    logout, profile access, password reset, and social login buttons.
    """
    def setUp(self):
        """
        Setup a test client and create a default test user.
        """
        self.client = Client()
        self.user_password = 'strongpassword123'
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password=self.user_password
        )

    def test_registration_page_loads(self):
        """
        Verify the registration (signup) page loads successfully and
        contains the expected content.
        """
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign Up")

    def test_user_can_register(self):
        """
        Test that a user can successfully register with valid credentials,
        and that a new user instance is created.
        """
        response = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'NewPass!234',
            'password2': 'NewPass!234',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_page_loads(self):
        """
        Verify the login page loads successfully and contains expected content.
        """
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_user_can_login(self):
        """
        Test that an existing user can log in using correct credentials,
        resulting in an authenticated session.
        """
        response = self.client.post(reverse('account_login'), {
            'login': self.user.username,
            'password': self.user_password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_can_logout(self):
        """
        Test that a logged-in user can log out successfully, resulting in a
        redirect.
        """
        self.client.login(
            username=self.user.username, password=self.user_password
            )
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)

    def test_user_profile_requires_login(self):
        """
        Verify that access to the user profile page requires authentication
        (redirects to login if not logged in).
        """
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_access_profile(self):
        """
        Verify that an authenticated user can access their profile page and
        sees relevant user data.
        """
        self.client.login(
            username=self.user.username, password=self.user_password
            )
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_password_reset_page_loads(self):
        """
        Verify the password reset page loads successfully and contains
        expected content.
        """
        response = self.client.get(reverse('account_reset_password'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Password Reset")

    def test_password_reset_email_sent(self):
        """
        Test that submitting the password reset form with a registered email
        sends a password reset email.
        """
        response = self.client.post(reverse('account_reset_password'), {
            'email': self.user.email,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Password reset", mail.outbox[0].subject)

    def test_social_login_buttons_present(self):
        """
        Verify that the login page contains buttons or links for social login
        providers such as Google and Facebook.
        """
        response = self.client.get(reverse('account_login'))
        self.assertContains(response, 'Google')
        self.assertContains(response, 'Facebook')
        self.assertContains(response, 'X')
