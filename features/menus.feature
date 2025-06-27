Feature: Menu Management and Customer Selection

Background:
    Given an superuser is logged in
    And the standard menu exists and is active
    And a seasonal menu "Summer Specials" exists and is active
    And another seasonal menu "Christmas Season" exists and is inactive
    And the standard menu has a menu item "Ember Table Burger" with ingredients "Bun, Beef Burger, Lettuce, Tomato, Onion"
    And the menu "Summer Specials" has a menu item "Grilled Salmon" with ingredients "Salmon, Lemon, Herbs"

Scenario: Customer views available seasonal menus
    When the customer visits the menu page
    Then they should see "Menu" and "Summer Specials"
    And "Menu" should include "Ember Table Burger" with ingredients "Bun, Beef Burger, Lettuce, Tomato, Onion"
    And "Summer Specials" should include "Grilled Salmon" along with ingredients "Salmon, Lemon, Herbs"
    And they should not see "Christmas Season"

Scenario: Customer selects a menu during booking
    Given the customer is on the booking form
    When they select "Summer Specials"
    And submit the form
    Then the booking should be created with the selected menu

Scenario: Admin deactivates a menu
    When the admin deactivates the menu "Summer Specials"
    Then "Summer Specials" should not appear on the public menu list
    And should include "Grilled Salmon" along with ingredients "Salmon, Lemon, Herbs"

Scenario: Menu auto-renews yearly if enabled
    Given the menu "Summer Specials" has auto renew enabled and has ended
    When the daily menu update runs
    Then a new menu for next year should be created