# Manual Tests

This document outlines the testing done to check the website works, both frontend and backend.

---

## Backend Logic Flow Chart

### Admin

#### Entering /admin

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 1 | Login Page shown | User must login | Pass |
| 2a | User has admin privilieges and enters correct credentials | Logs them into the admin portal if credentials are correct which uses summernote | Pass |
| 2b | User has admin privilieges and enters incorrect credentials | Displays error message asking them to fill in correct username and password | Pass |
| 2c | User doesn't have admin privileges | Displays error message asking them to fill in correct username and password | Pass |

#### Managing Users

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 3 | Clicking User | Loads the list of users and you can see who is a staff and who isn't | Pass |
| 4 | Deleting a user | Loads a questioning page to confirm deletion | Pass |
| 5a | Confirm user is to be deleted | User is deleted | Pass |
| 5b | Confirm user is not to be deleted | Loads the user back to user page | Pass |

#### Managing Bookings

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 3 | Clicking Bookings | Loads the list of bookings | Pass |
| 4 | Clicking a booking | Loads a form with booking information | Pass |
| 5 | Can edit the booking status | When saving reloads to the Bookings page to see all bookings | Pass |
| 6 | Can edit the table they are assigned too | When saving reloads to the Bookings page to see all bookings | Pass |

#### Managing Customers

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 3 | Clicking Customers | Loads the list of customers | Pass |
| 4 | Clicking a customer id | Loads the custoemrs info | Pass |
| 5 | Can edit the custoemrs info | When savigns changes reloads to the Customers page to see all customers | Pass |
| 6 | Can delete customer | Loads a confirmation page | Pass |
| 7a | Confirm customer is to be deleted | Custoemr is deleted | Pass |
| 7b | Confirm custoemr is not to be deleted | Loads the user back to Customer page | Pass |

#### Managing Tables

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 3 | Clicking Tables | Loads the list of Tables | Pass |
| 4 | User can add a table | Click add Table and see Table Form | Pass |
| 5 | Can edit the Tables in list | When savigns changes reloads to the Tables page to see all tables | Pass |

### User and Customer

#### Signing Up

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 1 | When sign up form is filled out correctly (see [Sign Up](#sign-up-modal)) | User is created in the User section of the admin page and in the Customer section | Pass |

#### Logging In

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 1 | When logging in is filled out correctly (see XXXX) | The password and username are checked against the Users | Pass |

### Booking

#### Making a Booking

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 1 | When make a booking form is filled out correctly (see XXXX) | Booking is submitted to the restaurant and they can edit the status | Pass |

#### Update a Booking

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 1 | When update a booking form is filled out correctly (see XXXX) | Booking is updated in the system and ready for the restaurant to review | Pass |

#### Cancel a Booking

| Step | Action | Outcome | Pass / Fail |
| ----- | ----- | ----- | ----- |
| 1 | When cancel a booking form is filled out correctly (see XXXX) | Booking is cancelled and the restaurant can see it in the system | Pass |

---

## Frontend Feature Testing

### Navbar

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| Navbar Page Indication | Page they are on is bold, a golden colour and underlined to indicate to users they are on that page | Pass |
| Navbar Clicking Logo | Loads the homepage | Pass |
| Navbar Clicking Home | Loads the homepage | Pass |
| Navbar Clicking Bookings | Loads the Booking Page | Pass |
| Navbar - If not logged in nor registered - Clicking Members | Loads the Members Info Page | Pass |
| Navbar - If logged in - Clicking Username | Loads the Members Dashboard and shows all bookings | Pass |
| Navbar - If logged in - Clicking Logout | Loads the Logout Modal | Pass |

### Logout Modal

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| Clicking Cancel | Leaves user on current page | Pass |
| Clicking Logout | Logs user out and loads homepage showing a success message to logging out | Pass |

### Homepage

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| Animated Background at top of page | The page at the tope has an animated gradient background | Pass |
| Clicking Book Now Buttons (either) | Takes user to booking page | Pass |
| Clicking Book Members Button - If not logged in nor registered  | Takes user to Members Info Page | Pass |
| Clicking Book Members Button - If logged in  | Takes user to Members Dashboard and shows all bookings | Pass |

### Booking Page

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| Animated Background at top of page | The page at the tope has an animated gradient background | Pass |
| If user is not logged in nor registered | Shows Sign Up and Login Buttons | Pass |
| Clicking Sign Up Button (either) | Opens Sign Up Modal | Pass |
| Clicking Login Button (either) | Opens Login Modal | Pass |
| If user is logged in | Shows Book and Dashboard buttons | Pass |
| Clicking Book Button (either) | Opens Make a Booking Modal | Pass |
| Clicking Dashboard Button | Takes user to Members Dashboard and shows all bookings | Pass |

### Sign Up Modal

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| If username is not filled out | Form won't submit | Pass |
| If First Name is not filled out | Form won't submit | Pass |
| If Last Name is not filled out | Form won't submit | Pass |
| If Email is not filled out | Form won't submit | Pass |
| If Email doesn't have the right credentials for an email e.g. no @ symbol | Form won't submit | Pass |
| If Phone is not filled out | Form won't submit | Pass |
| If Phone is not a number (UK or International with a +) | Form won't submit | Pass |
| If Password is not filled out | Form won't submit | Pass |
| If Confirm Password is not filled out | Form won't submit | Pass |
| Clicking Sign Up once all fields are filled out | Form submits and loads the page the sign up button was clicked on with a welcome message | Pass |

### Login Modal

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| If username is not filled out | Form won't submit | Pass |
| If Password is not filled out | Form won't submit | Pass |
| If either username nor password are correct | Error message appears asking them to login again | Pass |
| Clicking Login once all fields are filled out with correct credentials | Form submits and loads the page the sign up button was clicked on with a welcome back message | Pass |

### Booking Form Modal

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| If date is not filled out | Form won't submit | Pass |
| If time is not filled out | Form won't submit | Pass |
| If party size is not filled out | Form won't submit | Pass |
| If date is not today's nor a future date | Error message will appear | Pass |
| If time is not between 12pm and 10pm | Error message will appear | Pass |
| If party size is 0 or above 20 | Error message will appear | Pass |
| If all criteria is correct | Form will submit, success mesage shown with reference code and dashboard page loads with booking there | Pass |


### Members Page

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| Animated Background at top of page | The page at the tope has an animated gradient background | Pass |
| If user is not logged in nor registered | Shows Sign Up and Login Buttons with the perks of being a member | Pass |
| Clicking Sign Up Button (either) | Opens Sign Up Modal | Pass |
| Clicking Login Button (either) | Opens Login Modal | Pass |
| If user is logged in and has no pending, confirmed or unavailable bookings | Shows Book Now button | Pass |
| Clicking Book Now Button | Takes them to the bookings page | Pass |
| If user is logged in and has pending, confirmed or unavailable bookings | Shows all their bookings with cancel and update buttons | Pass |
| Clicking Cancel Button | Opens cancel form modal with Yes and No buttons | Pass |
| Clicking Update Button | Opens update form modal with pre filled out credentials | Pass |

### Cancel Modal

| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| If Yes is clicked | Form submits and booking is cancelled and removed from their dashboard view | Pass |
| If No is clicked | Modal will close and stay on the Dashboard with all bookings | Pass |

### Update Modal

Follow [Booking Form Modal](#booking-form-modal)
| Action | Outcome | Pass / Fail |
| ----- | ----- | ----- |
| If all information is valid | Form submits and booking is updated, success message shown and update is shown in the dashboard view | Pass |
| If close is clicked | Form is closed and user stays on dashboard | Pass |