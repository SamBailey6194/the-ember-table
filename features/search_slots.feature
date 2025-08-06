Feature: Search Booking Slots 

Background:
    Given there are tables available in the system

Scenario: User enters a valid date and sees available slots
    When the user searches for bookings on "2025-01-07"
    Then the system shows all available booking times

Scenario: User searches a date with no availability
    When the user searches for bookings on "26-12-2025"
    Then the system shows a message saying no slots available