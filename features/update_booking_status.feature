Feature: Update Booking Status

Background:
    Given an admin user is logged in
    And a booking exists with status "pending"

Scenario: Admin selects booking and updates booking to "confirmed"
    When the admin selects the booking
    And updates the status to "confirmed"
    Then the booking status should be updated to "confirmed"
    And the user should receive a confirmation email

Scenario: Admin selects booking and updates booking to "unavailable"
    When the admin selects the booking
    And updates the status to "unavailable"
    Then the booking status should be updated to "unavailable"
    And the user should receive an apology email stating booking is unavailable

Scenario: Admin selects booking and updates booking to "seated"
    When the admin selects the booking
    And updates the status to "seated"
    Then the booking status should be updated to "seated"