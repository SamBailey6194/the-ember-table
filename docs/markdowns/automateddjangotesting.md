# Automated Tests

This document outlines the automated backend tests written for the Django Apps using Django’s TestCase.

All tests were executed and passed successfully.

---

## Backend Unit Tests

### Forms

#### Make Booking Form

| Step | Action                                                              | Outcome                 | Pass / Fail |
| ---- | ------------------------------------------------------------------- | ----------------------- | ----------- |
| 1    | Submit with valid date, time (between 12–22), and party size (1–20) | Form is valid           | Pass        |
| 2    | Submit with party size = 0 or > 20                                  | Validation error raised | Pass        |
| 3    | Submit with date in the past                                        | Validation error raised | Pass        |
| 4    | Submit with time outside 12–22 (e.g. 09:00)                         | Validation error raised | Pass        |

#### Cancel Booking Form

| Step | Action                                             | Outcome                 | Pass / Fail |
| ---- | -------------------------------------------------- | ----------------------- | ----------- |
| 1    | Submit with valid reference code (booking exists)  | Form is valid           | Pass        |
| 2    | Submit with invalid or non-existent reference code | Validation error raised | Pass        |

#### Update Booking Form

| Step | Action                                            | Outcome                 | Pass / Fail |
| ---- | ------------------------------------------------- | ----------------------- | ----------- |
| 1    | Submit with valid reference code and updated data | Booking updated         | Pass        |
| 2    | Submit with invalid reference code                | Validation error raised | Pass        |
| 3    | Submit with past date                             | Validation error raised | Pass        |
| 4    | Submit with invalid time (outside 12–22)          | Validation error raised | Pass        |

### Models

#### Customer

| Step | Action                           | Outcome                             | Pass / Fail |
| ---- | -------------------------------- | ----------------------------------- | ----------- |
| 1    | Create customer linked to `User` | `__str__` returns username          | Pass        |
| 2    | Create guest customer (no user)  | `__str__` returns full name (Guest) | Pass        |

#### Table

| Step | Action                              | Outcome                            | Pass / Fail |
| ---- | ----------------------------------- | ---------------------------------- | ----------- |
| 1    | Create table with number & capacity | `__str__` returns formatted string | Pass        |


#### Booking

| Step | Action                                    | Outcome                                                    | Pass / Fail |
| ---- | ----------------------------------------- | ---------------------------------------------------------- | ----------- |
| 1    | Create booking linked to customer & table | `__str__` returns reference code, customer, date, and time | Pass        |
| 2    | Check default status                      | Booking status defaults to `pending`                       | Pass        |
| 3    | Check `reference_code`                    | Automatically generated unique UUID                        | Pass        |

### Views

#### Booking Page

| Step | Action                 | Outcome                                   | Pass / Fail |
| ---- | ---------------------- | ----------------------------------------- | ----------- |
| 1    | GET request            | Renders booking page with form in context | Pass        |
| 2    | POST with invalid form | Page reloads with error messages          | Pass        |


#### Make Booking

| Step | Action                           | Outcome                                                 | Pass / Fail |
| ---- | -------------------------------- | ------------------------------------------------------- | ----------- |
| 1    | POST valid data (logged in user) | Booking created, success message, redirect to dashboard | Pass        |
| 2    | POST invalid data                | Error message displayed, redirect to booking page       | Pass        |
| 3    | GET request                      | Returns modal with empty form                           | Pass        |

#### Cancel Booking

| Step | Action                                     | Outcome                                            | Pass / Fail |
| ---- | ------------------------------------------ | -------------------------------------------------- | ----------- |
| 1    | POST valid reference code (logged in user) | Booking status set to `cancelled`, success message | Pass        |
| 2    | POST invalid reference code                | Error message shown                                | Pass        |

#### Update Booking

| Step | Action                         | Outcome                                        | Pass / Fail |
| ---- | ------------------------------ | ---------------------------------------------- | ----------- |
| 1    | POST valid data                | Booking updated, success message               | Pass        |
| 2    | POST invalid data              | Error message displayed                        | Pass        |
| 3    | Access non-existent booking ID | Error message “Booking not found” and redirect | Pass        |