Feature: User Authentication

Background:
    Given the site is running
    And a user exists with username "testuser" and password "securepass"

Scenario: User logs in successfully
    When the user navigates to the login page
    And enters username "testuser" and password "securepass"
    And submits the login form
    Then they should be redirected to the dashboard
    And they should see "Welcome, testuser"
    And they can manage their bookings by creating a new one, cancelling one, or updating one

Scenario: User enters incorrect credentials
    When the user navigates to the login page
    And enters username "testuser" and password "wrongpass"
    And submits the login form
    Then they should see "Please enter a correct username and password"

Scenario: User logs out
    Given the user is logged in
    When the user clicks the logout button
    Then they should be redirected to the homepage
    And see "You have been logged out"
