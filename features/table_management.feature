Feature: Update Booking Status

Background:
    Given an admin user is logged in
    And table exists with number "1"
    And a booking exists with no table assigned

Scenario: Admin assigns a booking a table
    When the admin selects the booking
    And assigns table "1"
    Then the booking should be updated with table "1"