from behave import given, when, then
from selenium.webdriver.common.by import By
from django.core import mail
from django.contrib.auth.models import User
from booking.models import Booking, Table, Customer
from menus.models import Menu


@given('a booking exists with status "{status}" and menu "{menu_name}"')
def step_create_booking_with_status(context, status, menu_name):
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
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        menu = Menu.objects.get(is_seasonal=False)
    context.booking = Booking.objects.create(
        customer=customer,
        date="2025-12-01",
        time="18:00",
        menu=menu,
        party_size=2,
        status=status,
    )


@given('a table exists with number "{table_number}"')
def step_create_table(context, table_number):
    """
    Creates a table instance for BDD tests
    """
    context.table = Table.objects.create(number=int(table_number), capacity=4)


@given('I am a logged-in customer')
def step_logged_in_customer(context):
    """
    Logs in an existing user for booking interactions
    """
    context.browser.get(context.get_url('/accounts/login/'))
    context.browser.find_element(By.NAME, 'login').send_keys(
        'customer@example.com'
        )
    context.browser.find_element(By.NAME, 'password').send_keys(
        'testpassword123'
        )
    context.browser.find_element(By.ID, 'login-button').click()


@given('I have an existing booking')
def step_create_existing_booking(context):
    """
    Create a booking to be canceled
    """
    user = User.objects.get(email='customer@example.com')
    booking = Booking.objects.create(
        customer=user.customer,
        date="2025-08-15",
        time="19:00",
        party_size=2,
        status='confirmed',
    )
    context.existing_booking = booking


@when('the admin selects the booking')
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


@when('I visit the booking page')
def step_visit_booking_page(context):
    """
    User visits booking search page
    """
    context.browser.get(context.get_url('/booking/'))


@when('I select a date and time slot')
def step_select_date_time(context):
    """
    User selects a date and available time slot
    """
    context.browser.find_element(By.ID, 'date').send_keys('2025-08-20')
    context.browser.find_element(By.CLASS_NAME, 'slot-button').click()


@when('I confirm the booking')
def step_confirm_booking(context):
    """
    Confirm the booking on the booking form
    """
    context.browser.find_element(By.ID, 'confirm-booking-button').click()


@when('I go to my bookings page')
def step_go_to_bookings(context):
    """
    User visits their booking history page
    """
    context.browser.get(context.get_url('/booking/my-bookings/'))


@when('I click the cancel button for a booking')
def step_click_cancel(context):
    """
    Click the cancel button for a booking
    """
    context.browser.find_element(
        (By.CLASS_NAME, 'cancel-booking-button').click()
        )


@then('the booking status should be updated to "{expected_status}"')
def step_verify_updated_status(context, expected_status):
    """
    Confirm the booking status was updated in the database
    """
    context.booking.refresh_from_db()
    assert context.booking.status == expected_status


@then('a booking confirmation email should be sent to the customer')
def step_check_email_sent(context):
    """
    An email sent to confirm the booking
    """
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert "Booking Confirmation" in email.subject
    assert "testuser@example.com" in email.to
    assert "Booking confirmed" in email.body


@then('an apology email should be sent to the customer')
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


@then('I should see a list of available time slots')
def step_see_slots(context):
    """
    Page should show available time slots
    """
    slots = context.browser.find_elements(By.CLASS_NAME, 'slot-button')
    assert len(slots) > 0, "No time slots found."


@then('I should see a confirmation message')
def step_see_confirmation_message(context):
    """
    Booking confirmation is shown on success
    """
    message = context.browser.find_element(By.ID, 'confirmation-message').text
    assert "Booking confirmed" in message


@then('the booking should be marked as cancelled')
def step_booking_cancelled(context):
    """
    Ensure booking status is updated
    """
    context.existing_booking.refresh_from_db()
    assert context.existing_booking.status == "cancelled"
