Feature: Social Login

Background:
    Given the site is running
    And the user wants to register with a social login

Scenario: User logs in with Google
    When the user clicks "Login with Google"
    Then they should be redirected to their Google account
    And return logged in as a user

Scenario: User logs in with Facebook
    When the user clicks "Login with Facebook"
    Then they should be redirected to their Facebook account
    And return logged in as a user

Scenario: User logs in with X(Twitter)
    When the user clicks "Login with X"
    Then they should be redirected to their X account
    And return logged in as a user