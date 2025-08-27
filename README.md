# The Ember Table

**The Ember Table**

The decision to make this website is due to the user stories found [here](docs/markdowns/userstories.md).

You can also see how the user stories were made into sprints [here](docs/markdowns/plannedsprints.md).

As we progressed in the project some of the sprints were skipped due to time. You can see more in [Features](#features) section, especially [Features Left to Implement](#features-left-to-implement).

The design and layout is due to the wireframes shown below:

![Homepage Wireframe](docs/images/home_page.png)

![Menus Wireframe](docs/images/current_menus.png)

![Bookings Wireframe](docs/images/booking.png)

![Guest Booking Wireframe](docs/images/guest_booking_form.png)

![Login Wireframe](docs/images/login.png)

![Table Booking Wireframe](docs/images/table_booking.png)

Alongside the user stories, sprints and wireframes ERDs were made and a logic flow chart.

![ERDs](docs/images/erds.png)

![Logic Flow Chart](docs/images/logic_flow_chart.jpg)

As you venture to look at the [Features](#features) you will notice some design choices, logic flow and relationships between the database tables were changed while the project was being made.

I would usually put a Am I Responsive screenshot here. However, it wasn't loading the image correctly and even when tested with the Django Blog walkthrough project it wouldn't load the images properly. Due to time constraints I couldn't look into this further.

## Features 

Below are the features for the website and at the end is listed any features that weren't able to be implemented but would be with more time.

### Existing Features

- __Navbar__

  - The navbar is dynamic for mobile and non mobile views.
  - The navbar is also dynamic depending on if a user is authenticated or not.

  - __Screen Navbar__

    - Unauthenticated User View
      - On wider screens you can see the Logo, Home, Bookings and Members in the Navbar.
      - The page the user is on is underlined and made bold to indicate the page the user is on.

    - Authenticated User View
      - On wider screens you can see the Logo, Home, Bookings, Username and Logout in the Navbar.
      - The page the user is on is underlined and made bold to indicate the page the user is on.

    - General
      - When clicking the Logo you will be redirected to the homepage.
      - When clicking Home, Bookings, Members or Username you are loaded onto the relevant page you clicked.
        - For the username you are loaded onto the members dashboard.
      - For logout you see the logout modal to confirm you want to logout.

    ![Screen Navbar unauthenticated User](docs/images/screen_navbar_unauthenticated.png)

    ![Screen Navbar authenticated User](docs/images/screen_navbar_authenticated.png)

  - __Mobile Navbar__

    - General
      - On mobile screens you can see the Logo and a burger menu.
      - When clicking the Logo you will be redirected to the homepage.
      - When clicking the burger menu you see a dropdown with the pages available and is dynamic if the user is authenticated or not.
      - For logout you see the logout modal to confirm you want to logout.

    - Unauthenticated User View Dropdown
      - On wider screens you can see the Home, Bookings and Members in the Dropdown Navbar.
    
    - Authenticated User View Dropdown
      - On mobile screens you can see the Home, Bookings, Username and Logout in the Dropdown Navbar.

    ![Mobile Navbar](docs/images/mobile_navbar_unauthenticated.png)

    ![Mobile Navbar unauthenticated User](docs/images/mobile_navbar_dropdown_unauthenticated.png)

    ![Mobile Navbar authenticated User](docs/images/mobile_navbar_dropdown_authenticated.png)

  - __Logout Form Modal__

    - When the user clicks logout a logout modal appears asking them to confirm.
    - If they click Cancel it closes and they stay on the same page.
    - If they click Logout they are logged out and the homepage is loaded with a success message.
    
    ![Logout Form Modal](docs/images/logout_confirm_modal.png)

    ![Logout Success Modal](docs/images/logout_success.png)

- __Footer__

  - In the footer you have the address and contact information with the copyright info the the side on wider screens.
  - On mobile screens they stack on top of each other.
  - Clicking the email or phone will take the user to their mailing app or phone app.

  ![Screen Footer](docs/images/screen_footer.png)

  ![Mobile Footer](docs/images/mobile_footer.png)

- __Homepage__

  - __Homepage Header__

    - The animated background is written using Tailwind CSS, this is used for consistency across all pages in the header
    - It welcomes the user to the site with the name of the restaurant in the header
    - A small tagline to make the user excited about visiting the restaurant
    - A Book Now button that links to the bookings page
    
    ![Homepage Header](docs/images/homepage_header.png)

  - __Homepage Body__

    - The body has two sections, first section is three cards and the second one is two cards.
    - Section 1 with the three cards all describe the appeal to attending the restaurant, they are side by side on wider screens and on narrower screens they stack on top of each other.
    - Section 2 with the two cards are showing how you book and the benefits of being a member.
    - Book card has a Book Now button that takes the user to the bookings page.
    - Members card has a Members button that takes them to the members page. 
    
    ![Homepage Body](docs/images/homepage_body.png)

- __Bookings__

  - __Bookings Header__

    - The background is again the animated background.
    - Encourages the user to sign up or login to make a booking.
    - When the user is unauthenticated it has the Sign Up and Login buttons.
    - Sign Up button opens the Sign Up modal.
    - Login button opens the Login modal.
    - When the user is authenticated you see a book button, when clicked opens the booking form modal.
    
    ![Bookings Header unauthenticated user](docs/images/bookings_header.png)

    ![Bookings Header authenticated user](docs/images/bookings_header_authenticated.png)

  - __Bookings Body__

    - Encourages the user to join the members club.
    - When the user is unauthenticated it has the Sign Up and Login buttons.
    - Sign Up button opens the Sign Up modal.
    - Login button opens the Login modal.
    - When the user is authenticated you see two cards one for booking and one for the members dashboard.
    - Booking one has a book button, when clicked opens the booking form modal.
    - Members dashboard one has a Dashboard button, when clicked takes them to their dashboard showing their bookings.
    
    ![Bookings Body unauthenticated user](docs/images/bookings_body.png)

    ![Bookings Body authenticated user](docs/images/bookings_body_authenticated.png)

  - __Bookings Form Modal__

    - The form has three fields required, date, time and party size.
    - The username, first name, last name, email and phone number is assigned knowing the user is logged in
    - If any of the fields are not filled it it shows an error askign them to fill it in
    - If the form is submitted fully filled out, but the date is a passed date and/or the time is not between 12pm and 10pm and/or the party size is below 1 or above 20 an error message is displayed and they need to open the form again.
    
    ![Bookings Form Modal](docs/images/booking_form_modal.png)

    ![Bookings Success Modal](docs/images/booking_form_success.png)

    ![Bookings Error Modal](docs/images/booking_form_error.png)

- __Members__

  - __Members Header__

    - Encourages the user to join the members club.
    - When the user is unauthenticated it has the Sign Up and Login buttons.
    - Sign Up button opens the Sign Up modal.
    - Login button opens the Login modal.
    
    ![Members Header unauthenticated user](docs/images/members_header_unauthenticated.png)

    ![Members Header authenticated user](docs/images/members_header_authenticated.png)

  - __Members Body__

    - Encourages the user to join the members club.
    - When the user is unauthenticated it has the Sign Up and Login buttons.
    - Sign Up button opens the Sign Up modal.
    - Login button opens the Login modal.
    - If the user is authenticated with no bookings the card displayed is one to encourage them to book, clicking book now takes them to the booking page.
    - If the user is authenticated with bookings that are not cancelled each booking is displayed on an individual card with the date, time, party size and the uuid generated reference code.
    - Each card also has a cancel and update button.
    - Clicking cancel opens a cancel confirmation modal.
    - Clicking update opens a update form modal with the date, time and party size pre filled out.
    
    ![Members Body unauthenticated user](docs/images/members_body_unauthenticated.png)

    ![Members Body authenticated user with no bookings](docs/images/dashboard_authenticated_without_bookings.png)

    ![Members Body authenticated user with bookings](docs/images/dashboard_authenticated_has_bookings.png)

  - __Cancel Form Modal__

    - Displays a modal with a Yes and No.
    - If yes clicked and the booking can be found in the database a success message is shown, the dashboard is reloaded and the cancelled booking is removed from the list of bookings.
    - If no clicked the modal closes and the user sees all their bookings again.
    
    ![Cancel Form Modal](docs/images/cancel_form_modal.png)

    ![Cancel Success Modal](docs/images/cancel_success.png)

  - __Update Form Modal__

    - Displays a modal with the date, time and party size of the linked booking for the user to edit
    - Buttons update and close are at the bottom.
    - If they attempt to change the date, time or party size to a value not allowed they won't being to submit the form.
    - Clicking update will reload dashboard and show a success message.
    
    ![Update Form Modal](docs/images/update_booking_modal.png)

    ![Update Success Modal](docs/images/update_success.png)

  - __Sign Up Form Modal__

    - A form with username, first name, last name, email, phone, password and confirm password appears.
    - All fields must be filled out correctly e.g. if the email doesn't have a @ and url.com it won't be valid.
    - If the username is taken an error message displays.
    - If the form is filled out correctly and username is not taken they see a success message and the page reloads.
    
    ![Sign Up Form Modal](docs/images/signup_form_modal.png)

    ![Sign Up Success Modal](docs/images/signup_success.png)

    ![Sign Up Error Modal](docs/images/signup_error.png)

  - __Login Form Modal__

    - This form opens and asks for username or email and the password linked to it.
    - If credentials match what is in the database a success message appears and user is logged in on reloaded page.
    - If credentials do not match what is in the database an error message appears and user is not logged in on reloaded page.
    
    ![Login Form Modal](docs/images/login_form_modal.png)

    ![Login Success Modal](docs/images/login_success.png)

    ![Login Error Modal](docs/images/login_error.png)

### Features Left to Implement

- Make

## Testing 

The website has been tested;

### Fixed Bugs

- C

### Unfixed Bugs

- Varying performance score on Lighthouse Mobile due to LCP and Render Blocking
  - The scores cary from in the 60s to the 90s

### Validator Testing 

- Lighthouse Score
  - Below you can see my lighthouse scores tested on Chrome Incognito Mode

  - Homepage Mobile

  ![Lighthouse - Homepage](XXX)

- HTML
  - No errors were returned when passing through the official W3C Validator, see images below for each page.

    - Homepage
      
    ![W3C validator - Homepage](XXX)

- CSS
  - Put CSS through Autoprefixer to ensure it works on all browsers
  - No errors were found when passing through the official Jigsaw validator, see links below.
  
   ![(Jigsaw) validator 1](XXX)

## Deployment

The app deployed via Heroku [here](XXX) following the below steps

### Version Notes
Before going to Heroku make sure the .python-version is at the correct version.

You can check this by:
1. Typing python --version or python3 --version in your terminal
2. Update the file .python-version to the correct version
   1. The python version for this project as of xx/xx/2025 is 3.13.5

Important note, before upgrading to latest python version, check all the dependencies and modules are accepted by that version.

Once you have the correct version of python installed and noted, you then need to install the correct versions of the dependencies and update requirements.txt.

To do the above follow below:
1. Install the correct versions of the dependencies and modules
2. For the correct dependencies use pip install "dependency/module name" or pip3 install "dependency/module name"
   1. If the dependency or module is an older version add =="version"
3. Then type pip freeze > requirements.txt or pip3 freeze > requirements.txt to update requirements.txt

### Creating the Heroku App
To create the app Heroku was used. In Heroku two buildpacks were needed and were accessed from the _Settings_ tab in Heroku. After adding the individual buildpacks the settings were saved. The two packs used and their ordering is as follows:

1. `heroku/python`

Then X config vars were needed and were created by going to _Settings_ tab in Heroku and scrolling down to _Config Var_ section. After each individual config var was added the settings were saved Then the following config vars were created: 

1. O

Then the GitHub repository was connected by following the below steps:

1. Go to _Deploy_ section
2. Select GitHub as the deployment method
3. Confirm we wanted to connect GitHub
4. Then search for the ultimate_battleships repository and connected it
5. Then in Manual deploy, select the main branch and click Deploy Branch, this should then deploy the app

## Cloning

This section describes how other software developers can clone the code to edit it elsewhere

- To clone the code so you can edit it yourself please follow the below:
PLEASE NOTE THIS IS FOR WINDOWS COMMAND LINE
  - In the GitHub repository click the dropdown for '<> code'
  - Ensure you are on 'local' and have 'https' selected, then copy the URL by clicking the symbol next to the URL box
  - Once copied in the search bar on your taskbar type in 'cmd' and open 'Command Prompt' or 'Comman Line'
  - In command line type 'git clone' and paste the url next to it
  - In file explorer locate 'This PC' down the side, then 'local disk' (usually the :C drive), then 'users', then your user, then find the folder called 'photo-guides'
  - You now have access to all the code and files locally
  - If you want to edit the code, please ensure you creat a new branch in the software you are using enabling us to potentially see the edits you have done before uploading them to the original GitHub repository
  - To create a new branch that depends on the software you are using, please google how to do this for your software

If you aren't on windows please google how to get a GitHub repository stored locally on your OS

 
## Credits 

Below are my credits for where I got inspiration for some of the code, where the content came from and where media is from.

### Code

- T

### Content 

- T

### Media

- M
