Feature: Password Reset

Background:
    Given a user exists with email "user@example.com"
    And have forgotten their password

Scenario: User requests a password reset
    When the user visits the password reset page
    And enters their email "user@example.com"
    And submits the password reset form
    Then they should see "We've emailed you instructions for setting your password"

Scenario: User resets password using link
    Given the user has received the reset email
    When they follow the reset link
    And enter a new password
    Then they should be able to log in with the new password
