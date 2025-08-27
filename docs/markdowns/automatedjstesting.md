# Automated JS Tests

This document outlines the automated frontend tests written for the JavaScript modules of the Ember Table website.  

All tests were executed from `theme/static_src` using `npm test` and passed successfully.

---

## Booking Modals (bookingModals.js)

### Cancel Booking Modal

| Step | Action                                             | Outcome                               | Pass / Fail |
| ---- | -------------------------------------------------- | ------------------------------------- | ----------- |
| 1    | Click cancel button on a booking                  | Modal opens, reference code populated | Pass        |
| 2    | Click close button on modal                        | Modal closes                           | Pass        |

### Update Booking Modal

| Step | Action                                              | Outcome                                           | Pass / Fail |
| ---- | --------------------------------------------------- | ------------------------------------------------- | ----------- |
| 1    | Click update button on a booking                    | Modal opens, form pre-filled with booking data  | Pass        |
| 2    | Submit update form                                  | Modal closes, booking updates triggered          | Pass        |
| 3    | Click cancel button on modal                        | Modal closes                                     | Pass        |

---

## Navbar (navbar.js)

### Burger Menu

| Step | Action                  | Outcome                           | Pass / Fail |
| ---- | ----------------------- | --------------------------------- | ----------- |
| 1    | Click burger menu button | Mobile menu toggles visibility   | Pass        |
| 2    | Click again              | Mobile menu toggles back hidden  | Pass        |

### Logout Modal

| Step | Action                        | Outcome                        | Pass / Fail |
| ---- | ----------------------------- | ------------------------------ | ----------- |
| 1    | Click logout button           | Logout modal opens             | Pass        |
| 2    | Click close button on modal   | Logout modal closes            | Pass        |

---

## Alert Modal (alert.js)

| Step | Action                         | Outcome                             | Pass / Fail |
| ---- | ------------------------------ | ----------------------------------- | ----------- |
| 1    | Call `showMessage(title, body)` | Modal opens, title and body set     | Pass        |