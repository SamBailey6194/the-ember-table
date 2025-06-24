from behave import given, when, then
from selenium.webdriver.common.by import By
from django.core import mail
from booking.models import Booking, Table, Customer


@given('a booking exists with status "{status}"')
def step_create_booking_with_status(context, status):
    """
    Created fake customer and fake booking for tests
    """
    customer = Customer.objects.create(
        is_guest=True,
        customer_fname="Test",
        customer_lname="Name",
        email="testuser@example.com",
        phone="0123456789"
    )
    context.booking = Booking.objects.create(
        customer=customer,
        date="2025-12-01",
        time="18:00",
        party_size=2,
        status=status,
    )


@given('a table exists with number "{table_number}"')
def step_create_table(context, table_number):
    """
    Creates a table instance for BDD tests
    """
    context.table = Table.objects.create(number=int(table_number), capacity=4)


@when('teh admin selects the booking')
def step_admin_selects_booking(context):
    """
    Open the admin change form for the test booking
    """
    context.browser.get(context.get_url(
        f"/admin/booking/booking/{context.booking.id}/change"
        ))


@when('updates the status to "{new_status}"')
def step_update_status(context, new_status):
    """
    Change the booking status on the admin form
    """
    status_dropdown = context.browser.find_element(By.NAME, "status")
    status_dropdown.send_keys(new_status)
    context.browser.find_element(By.NAME, "_save").click()


@when('assigns table "{table_number}"')
def step_assign_table(context, table_number):
    """
    Assign a table number to the booking using the admin form
    """
    context.browser.get(context.get_url(
        f"/admin/booking/booking/{context.booking.id}/change"
        ))
    table_dropdown = context.browser.find_element(By.NAME, "table")
    table_dropdown.send_keys(table_number)
    context.browser.find_element(By.NAME, "_save").click()


@then('the booking status should be updated to "{expected_status}"')
def step_verify_updated_status(context, expected_status):
    """
    Confirm the booking status was updated in the database
    """
    context.booking.refresh_from_db()
    assert context.booking.status == expected_status


@then('an email should be sent to the customer')
def step_check_email_sent(context):
    """
    An email sent to confirm the booking
    """
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert "Booking Confirmation" in email.subject
    assert "testuser@example.com" in email.to
    assert "Booking confirmed" in email.body


@then('an email should be sent to the customer')
def step_check_unavailable_email(context):
    """
    An email sent to apologise the booking is unavailable
    """
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert "Booking Unavailable" in email.subject
    assert "testuser@example.com" in email.to
    assert "We're sorry the booking slot is unavailable" in email.body


@then('the booking should be updated with table "{expected_table}"')
def step_verify_table_assignment(context, expected_table):
    """
    Confirm the booking's table was assigned correctly
    """
    context.booking.refresh_from_db()
    assert context.booking.table.number == int(expected_table)
