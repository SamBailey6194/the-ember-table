import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# Defining folder to save screenshots of failed tests in
SCREENSHOTS_DIR = "screenshots"


def before_all(context):
    """
    Runs before the BDD tests start. Determines if the tests are run in Chrome
    headless or not. Then sets options for Chrome accordingly and enables
    better compatibility with all OS's, especially Linux. Service object is
    created and then launches Chrome browser. Finally creates screenshots
    directory if one doesn't exist.
    """
    headless = os.getenv("HEADLESS", "true").lower() in ("true", "1", "yes")
    options = Options()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    service = Service()
    context.browser = webdriver.Chrome(service=service, options=options)
    context.browser.implicitly_wait(10)
    context.get_url = lambda path: context.test_case.live_server_url + path

    # Make sure screenshots dir exists
    if not os.path.exists(SCREENSHOTS_DIR):
        os.makedirs(SCREENSHOTS_DIR)


def after_all(context):
    """
    Runs after the BDD tests have ran and then quits the browser.
    """
    if hasattr(context, 'browser'):
        context.browser.quit()


def before_scenario(context, scenario):
    """
    Runs before each individual test scenario to set up a fresh Django
    live test server instance, to enable tests to have a real HTTP
    server to talk to
    """
    context.test_case = StaticLiveServerTestCase()
    context.test_case.setUpClass()


def after_scenario(context, scenario):
    """
    Runs after each scenario. Determines if the scenario failed or passed.
    IF failed:
        Cleans the scnerio
        Saves a Screenshot
        Prints a console message
    IF passed:
        Tears down the live server instance to reset state before the next test
    """
    if scenario.status == 'failed':
        safe_name = "".join(
            c if c.isalnum() or c in (" ", "_") else "_" for c in scenario.name
            )
        filename = f"{safe_name}.png"
        filepath = os.path.join(SCREENSHOTS_DIR, filename)
        context.browser.save_screenshot(filepath)
        print(f"\n[SCREENSHOT] Saved failure screenshot to {filepath}")

    context.test_case.tearDownClass()
