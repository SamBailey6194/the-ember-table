Feature: Admin Login

Background:
    Given an admin user exists with username "admin" and password "adminpass"

Scenario: Admin logs in with correct credentials
    When the admin visits the login page
    And submits the login form with correct credentials
    Then the admin should be redirected to the dashboard

Scenario: Admin logs in with incorrect credentials
    When the admin visits the login page
    And submits the login form with incorrect credentials
    Then the admin should see a login error message