Feature: Make Booking 

Background:
    Given there is an available table for 4 people at 18:00 on "07-01-2025"

Scenario: User successfully makes a booking
    When the user books a table for 4 on "07-01-2025" at 18:00
    Then the system confirms the booking with a reference

Scenario: User books a slot that's already taken
    When the user books the same table again
    Then the system shows a double booking error