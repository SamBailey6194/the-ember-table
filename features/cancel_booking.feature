Feature: Cancel Booking

Background:
    Given a booking exists with reference "ABC123"

Scenario: User cancels a valid booking
    When the user enters "ABC123" to cancel
    Then the booking is marked as cancelled
    And the system shows a success message

Scenario: User enters an invalid booking reference
    When the user enters "XYZ999" to cancel
    Then the system shows an error message