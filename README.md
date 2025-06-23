# The Ember Table

**The Ember Table**

The decision to make this website is due to the user stories found [here](docs/markdowns/userstories.md).

![Responsive Mockup](xxx)

## Features 

Below are the features for the website and at the end is listed any features that weren't able to be implemented but would be with more time.

### Existing Features

- __Home Page__

  - __Header__

    - This
    
    ![Homepage Header](XXX)

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
