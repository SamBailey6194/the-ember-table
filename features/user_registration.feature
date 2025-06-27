Feature: User Registration

Background:
    Given the site is running
    And the user want to register

Scenario: New user registers successfully
    When the user navigates to the registration page
    And enters username "newuser", email "newuser@example.com", and password "newpass123"
    And submits the registration form
    Then an account should be created for "newuser"
    And the user should be redirected to the login page



Scenario: Registration with mismatched passwords
    When the user navigates to the registration page
    And enters mismatched passwords
    And submits the registration form
    Then they should see "Passwords do not match"
