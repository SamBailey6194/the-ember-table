# The Ember Table User Stories and Business Goal

## The Ember Tale Business Goal

### Business Goal
To provide a seamless and memorable dining experience by combining high-quality cuisine, exceptional service, and a smart reservation system that maximizes table efficiency and guest satisfaction.

---

## User Stories

I have used the MoSCoW priority system and the fibonnachi story point sequence (1, 2, 3, 5, 8, 13, etc).

### US001: Search Booking Slots

**As a user**
**I want to** search for available booking slots by date
**So that** I can find a suitable time to make a reservation.

**Acceptance Criteria:**
- User can input a date to search for available slots.
- System validates the date format and rejects invalid dates.
- If no slots are available, user sees a clear message.
- Available slots are displayed clearly.

**Tasks:**
- Design booking slot data model.
- Create search form with date validation.
- Implement backend logic to query available slots.
- Build results page or message display.

**MoSCoW Priority:** Must Have

**Story Points:** 3

---

### US002: Make Booking

**As a user**
**I want to** make a booking by selecting a date, time, party size, and providing my contact info
**So that** I can reserve a table at the restaurant.

**Acceptance Criteria:**
- Booking form captures date, time, party size, and contact information.
- System prevents double booking on the same slot.
- On success, user sees a confirmation page with booking reference.
- Confirmation email is sent to the user.

**Tasks:**
- Develop booking form with validations.
- Implement logic to check slot availability and create booking.
- Create confirmation page UI.
- Integrate email service for confirmation emails.

**MoSCoW Priority:** Must Have

**Story Points:** 5

---

### US003: Cancel Booking

**As a user**
**I want to** cancel my booking using a reference number
**So that** I can free up the slot if I no longer need it.

**Acceptance Criteria:**
- User inputs booking reference number to cancel.
- System validates the reference number and booking exists.
- Booking is marked cancelled and slot freed.
- User receives confirmation or error message.

**Tasks:**
- Build cancellation form with validation.
- Implement lookup and cancellation logic.
- Update slot availability after cancellation.
- Display success or error messages.

**MoSCoW Priority:** Must Have

**Story Points:** 2

---

### US004: Admin Login

**As an admin**
**I want to** securely login to an admin dashboard
**So that** I can manage bookings and view restaurant reservations.

**Acceptance Criteria:**
- Admin login form requires username and password.
- Invalid credentials show error.
- Successful login redirects admin to dashboard page.

**Tasks:**
- Create login form and authentication backend.
- Implement error handling for failed logins.
- Build admin dashboard landing page.

**MoSCoW Priority:** Must Have

**Story Points:** 3

---

### US005: Update Booking Status

**As an admin**
**I want to** update the status of a booking (e.g., "Seated", "Cancelled")
**So that** I can track the progress of bookings accurately.

**Acceptance Criteria:**
- Admin can select and update booking status.
- Status changes are saved in the database.
- Optional email notification can be sent on status update.

**Tasks:**
- Build booking status update form in admin dashboard.
- Implement backend logic to update status.
- Integrate email notification (optional).

**MoSCoW Priority:** Must Have

**Story Points:** 3

---

### US006: User Account Registration and Login

**As a user**
**I want to** create an account and login
**So that** I can manage all my bookings in one profile.

**Acceptance Criteria:**
- Users can register, login, and logout.
- Users can view and modify bookings in their profile.
- Password recovery functionality is available.

**Tasks:**
- Design user authentication system.
- Build registration and login forms.
- Create user dashboard for managing bookings.

**MoSCoW Priority:** Must Have

**Story Points:** 5

---

### US007: Email Notifications

**As a user**
**I want to** receive email notifications about booking confirmations and updates
**So that** I am kept informed about my reservation.

**Acceptance Criteria:**
- Emails are sent upon booking creation and status updates.
- System handles email failures gracefully (e.g., retries, logs).

**Tasks:**
- Setup email backend service.
- Create email templates for confirmation and updates.
- Add error handling for email send failures.

**MoSCoW Priority:** Must Have

**Story Points:** 2

---

### US008: Seasonal Menu Selection

**As a user**
**I want to** view available seasonal menus and select one when booking
**So that** I can choose a menu that suits my occasion.

**Acceptance Criteria:**
- Customers can view only active seasonal menus.
- The booking form shows a dropdown of currently active menus.
- If no menu is selected, a default/general menu is assumed.

**Tasks:**
- Add SeasonalMenu model with is_active, start_date, and end_date.
- Display available menus on a public menu page.
- Add menu dropdown to booking form.
- Link selected menu to Booking.
- Write tests for form logic and display.

**MoSCoW Priority:** Must Have

**Story Points:** 5

---

### US009: Seasonal Menu Admin Control

**As a superuser**
**I want to** activate/deactivate seasonal menus and manage their dishes
**So that** I can keep menus current and ready for seasonal changes.

**Acceptance Criteria:**
- Superusers can toggle menu availability.
- Menu dates auto-renew yearly if set to repeat.
- Admins can create/edit/delete menu items linked to each menu.
- Each item includes name, description, ingredients, price, and availability status.

**Tasks:**
- Add auto_renew_yearly logic to SeasonalMenu.
- Create inline admin panel for managing MenuItems.
- Build a management command to auto-update active menus daily.
- Write admin filters for active/inactive menus.
- Add unit tests for rollover and availability logic.

**MoSCoW Priority:** Must Have

**Story Points:** 8

---

### US010: Social Media Login (Google, Facebook)

**As a user**
**I want to** log in using my social media accounts
**So that** I can register quickly.

**Acceptance Criteria:**
- OAuth login with Google and Facebook.
- Social accounts link to internal user profile.

**Tasks:**
- Integrate Google/Facebook login using social-auth.
- Map external profiles to internal user table.
- Handle edge cases like multiple accounts.

**MoSCoW Priority:** Should Have

**Story Points:** 3

---

### US011: Table Management

**As an admin**
**I want to** assign specific tables to bookings
**So that** I can better organize seating arrangements.

**Acceptance Criteria:**
- Admin can assign and view tables per booking.
- Dashboard shows table availability status.

**Tasks:**
- Add table model and booking-table relationship.
- Create UI for assigning tables.
- Integrate table availability tracking.

**MoSCoW Priority:** Should Have

**Story Points:** 5

---

### US012: Mobile App Integration

**As a user**
**I want to** use a mobile app connected to the booking system
**So that** I can make and manage bookings on the go.

**Acceptance Criteria:**
- Mobile app syncs booking data in real-time with the website system.

**Tasks:**
- Create mobile-friendly API endpoints.
- Build frontend mobile app (React Native or similar).
- Test syncing and data consistency.

**MoSCoW Priority:** Could Have

**Story Points:** 8

---

### US013: Payment Processing

**As a user**
**I want to** pay online to confirm my booking
**So that** I guarantee my reservation.

**Acceptance Criteria:**
- Online payment options integrated.
- Payment status reflected in booking record.
- User gets receipt and confirmation.

**Tasks:**
- Integrate Stripe/PayPal API.
- Update booking model with payment status.
- Secure payment form and callbacks.

**MoSCoW Priority:** Could Have

**Story Points:** 8

---

### US014: Advanced Reporting and Analytics

**As an admin**
**I want to** view detailed reports and analytics
**So that** I can analyze booking trends and customer behavior.

**Acceptance Criteria:**
- Admin dashboard shows charts and booking KPIs.
- Data export available in CSV/Excel.

**Tasks:**
- Aggregate booking data with Django ORM.
- Use chart libraries to visualize trends.
- Implement export feature.

**MoSCoW Priority:** Won’t Have

**Story Points:** 8