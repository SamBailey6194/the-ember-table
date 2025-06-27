from behave import given, when, then
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from django.contrib.auth.models import User
from django.core import mail


@given('the site is running')
def step_site_running(_context):
    """
    Placeholder for server running - used to satisfy Background
    """
    pass


@given('a user exists with username "{username}" and password "{password}"')
def step_create_user(_context, username, password):
    """
    Creates user for the tests
    """
    User.objects.create_user(
        username=username, email=f"{username}@example.com", password=password
        )


@given('a user exists with email "{email}"')
def step_create_user_by_email(_context, email):
    """
    Creates a user with email for user logins when password is not needed
    Such as when a guest customer wants to access their booking page
    """
    User.objects.create_user(
        username=email.split('@')[0], email=email, password='temp1234'
        )


@given('the user is logged in')
def step_user_is_logged_in(context):
    """
    Logs user in correctly
    """
    context.browser.get(context.get_url("/accounts/login/"))
    context.browser.find_element(By.NAME, "username").send_keys("testuser")
    context.browser.find_element(By.NAME, "password").send_keys("securepass")
    context.browser.find_element(By.XPATH, "//input[@type='submit']").click()


# --- LOGIN ---
@when('the user navigates to the login page')
def step_visit_login_page(context):
    """
    Navigates the user to the login page
    """
    context.browser.get(context.get_url("/accounts/login/"))


@when('enters username "{username}" and password "{password}"')
def step_enter_login_credentials(context, username, password):
    """
    Checks that login credentials work
    """
    context.browser.find_element(By.NAME, "username").send_keys(username)
    context.browser.find_element(By.NAME, "password").send_keys(password)


@when('submits the login form')
def step_submit_login_form(context):
    """
    Login in form is submitted
    """
    context.browser.find_element(By.XPATH, "//input[@type='submit']").click()


@then('they should be redirected to the dashboard')
def step_redirect_dashboard(context):
    """
    After logging in they are redirected to the dashboard
    """
    assert "/dashboard" in context.browser.current_url


@then('they should see "Welcome, {username}"')
def step_see_welcome(context, username):
    """
    Once logged in they are shown a welcome message
    """
    assert f"Welcome, {username}" in context.browser.page_source


@then('they should see "Please enter a correct username and password"')
def step_login_error(context):
    """
    When login credentials don't match
    """
    assert (
        "Please enter a correct username and password" in
        context.browser.page_source
        )


# --- LOGOUT ---
@when('the user clicks the logout button')
def step_click_logout(context):
    """
    Checks the logout button works
    """
    context.browser.get(context.get_url("/accounts/logout/"))


@then('they should be redirected to the homepage')
def step_redirect_home(context):
    """
    Checks they are redirected to the homepage
    """
    assert context.get_url("/") in context.browser.current_url


@then('see "You have been logged out"')
def step_logged_out_message(context):
    """
    A message appears stating they were logged out
    """
    assert "You have been logged out" in context.browser.page_source


# --- REGISTRATION ---
@when('the user navigates to the registration page')
def step_visit_register_page(context):
    """
    A user goes to the registration page to create an account
    """
    context.browser.get(context.get_url("/accounts/register/"))


@when(
        'enters username "{username}", email "{email}", '
        'and password "{password}"'
        )
def step_fill_register_form(context, username, email, password):
    """
    Registration form is filled in
    """
    context.browser.find_element(By.NAME, "username").send_keys(username)
    context.browser.find_element(By.NAME, "email").send_keys(email)
    context.browser.find_element(By.NAME, "password1").send_keys(password)
    context.browser.find_element(By.NAME, "password2").send_keys(password)


@when('enters mismatched passwords')
def step_register_mismatched_passwords(context):
    """
    Enters mismatched passwords into the two password fields
    """
    context.browser.find_element(By.NAME, "username").send_keys("newuser")
    context.browser.find_element(By.NAME, "email").send_keys(
        "newuser@example.com"
        )
    context.browser.find_element(By.NAME, "password1").send_keys("pass123")
    context.browser.find_element(By.NAME, "password2").send_keys(
        "differentpass"
        )


@then('an account should be created for "{username}"')
def step_account_created(_context, username):
    """
    If all information is correct and passwords match account is created
    """
    assert User.objects.filter(username=username).exists()


@then('the user should be redirected to the login page')
def step_redirect_to_login(context):
    """
    Once new account is created they are redirected to the login page
    """
    assert "/accounts/login" in context.browser.current_url


@then('they should see "Passwords do not match"')
def step_password_mismatch_error(context):
    """
    If passwords do not match they receive an error
    """
    assert "Passwords do not match" in context.browser.page_source


# --- PASSWORD RESET ---
@when('the user visits the password reset page')
def step_visit_password_reset(context):
    """
    User goes to reset their passwords
    """
    context.browser.get(context.get_url("/accounts/password_reset/"))


@when('enters their email "{email}"')
def step_enter_reset_email(context, email):
    """
    Checks they can enter their email
    """
    context.browser.find_element(By.NAME, "email").send_keys(email)


@when('submits the password reset form')
def step_submit_reset_form(context):
    """
    If email exists user is sent an email with a reset form
    """
    context.browser.find_element(By.XPATH, "//input[@type='submit']").click()


@then(
        'they should see "We\'ve emailed you instructions '
        'for setting your password"'
        )
def step_password_reset_email_sent(context):
    """
    Message shown to user that the password reset email has been sent to them
    """
    assert (
        "We've emailed you instructions for setting your password"
        in context.browser.page_source
        )


@then('the user has received the reset email')
def step_check_email_received(_context):
    """
    User receives the reset email
    """
    assert len(mail.outbox) == 1
    assert "Password reset" in mail.outbox[0].subject


# --- SOCIAL LOGIN ---
@then('they should see a "Google" login button')
def step_check_google_button(context):
    """
    Check there is a login button for Google
    """
    google_button = context.browser.find_element(
        By.CSS_SELECTOR, 'a.socialaccount_provider.google'
        )
    assert google_button is not None
    assert "google" in google_button.get_attribute("href")


@then('they should see a "Facebook" login button')
def step_check_facebook_button(context):
    """
    Check there is a login button for Facebook
    """
    facebook_button = context.browser.find_element(
        By.CSS_SELECTOR, 'a.socialaccount_provider.facebook'
        )
    assert facebook_button is not None
    assert "facebook" in facebook_button.get_attribute("href")


@then('they should see a "X" login button')
def step_check_x_button(context):
    """
    Check there is a login button for X (Twitter)
    """
    x_button = context.browser.find_element(
        By.CSS_SELECTOR, 'a.socialaccount_provider.x'
        )
    assert x_button is not None
    assert "x" in x_button.get_attribute("href")


@when('they click the "Google" login button')
def step_click_google_login(context):
    """
    Check there is a login button for Google
    """
    google_button = context.browser.find_element(
        By.CSS_SELECTOR, 'a.socialaccount_provider.google'
        )
    google_button.click()


@then('they should be redirected to the Google login endpoint')
def step_check_google_redirect(context):
    parsed_url = urlparse(context.browser.current_url)
    assert (
        "accounts.google.com" in parsed_url.netloc or "google.com"
        in parsed_url.netloc
        )


@when('they click the "Facebook" login button')
def step_click_facebook_login(context):
    facebook_button = context.browser.find_element(
        By.CSS_SELECTOR, 'a.socialaccount_provider.facebook'
        )
    facebook_button.click()


@then('they should be redirected to the Facebook login endpoint')
def step_check_facebook_redirect(context):
    parsed_url = urlparse(context.browser.current_url)
    assert "facebook.com" in parsed_url.netloc


@when('they click the "x" login button')
def step_click_x_login(context):
    x_button = context.browser.find_element(
        By.CSS_SELECTOR, 'a.socialaccount_provider.x'
        )
    x_button.click()


@then('they should be redirected to the X login endpoint')
def step_check_x_redirect(context):
    parsed_url = urlparse(context.browser.current_url)
    assert "x.com" in parsed_url.netloc
