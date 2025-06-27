from behave import given, when, then
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User


@given(
    'an admin user exists with username "{username}" '
    'and password "{password}"')
def step_create_admin_user(context, username, password):
    """
    Creating a user
    """
    User.objects.create_superuser(
        username=username, email='admin@example.com', password=password
        )


@when('the admin visits the login page')
def step_visit_login(context):
    """
    Giving the test access to admin login page
    """
    context.browser.get(context.get_url("/admin/login/"))


@when('submits the login form with correct credentials')
def step_submit_valid_login(context):
    """
    Checks valid login
    """
    context.browser.find_element(By.NAME, "username").send_keys("admin")
    context.browser.find_element(By.NAME, "password").send_keys("adminpass")
    context.browser.find_element(By.XPATH, "//input[@type='submit']").click()


@when('submits the login form with incorrect credentials')
def step_submit_invalid_login(context):
    """
    Checks for invalid login
    """
    context.browser.find_element(By.NAME, "username").send_keys("admin")
    context.browser.find_element(By.NAME, "password").send_keys("wrongpass")
    context.browser.find_element(By.XPATH, "//input[@type='submit']").click


@then('the admin should be redirected to the dashboard')
def step_redirect_to_dashboard(context):
    """
    Checks admin is redirected to dashboard
    """
    assert "/admin/" in context.browser.current_url
    assert "Site administration" in context.browser.page_source


@then('the admin should see a login error message')
def step_see_login_error(context):
    """
    Checks admin is shown error message if they use invalid credentials
    """
    assert (
        "Please enter the correct username and password"
        in context.browser.page_source
        )
