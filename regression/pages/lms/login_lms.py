"""
LMS login page
"""
from edxapp_acceptance.pages.lms.login import LoginPage
from edxapp_acceptance.pages.lms.dashboard import DashboardPage
from regression.pages.lms import LOGIN_BASE_URL
from regression.pages.lms.dashboard_lms import DashboardPageExtended
import time


class LmsLogin(LoginPage):
    """
    This class is an extended class of LoginPage,
    where we add methods that are different or not used in LoginPage
    """
    url = 'http://edx.devstack.lms:18000' + '/login'

    def is_browser_on_page(self):
        """
        Verifies if the browser is on the correct page
        """
        return self.q(css='.js-login.login-button').visible

    def provide_info(self, email, password):
        """
        Fill in login info
        'Username' and 'Password' are the user's credentials
        """
        email_selector = 'input#login-email'
        password_selector = 'input#login-password'
        
        time.sleep(30)
        self.wait_for_element_visibility(
            email_selector, 'Email input area present')
        self.wait_for_element_visibility(
            password_selector, 'Password input are present')

        self.q(css=email_selector).fill(email)
        self.q(css=password_selector).fill(password)
        self.wait_for_ajax()

    def submit(self):
        """
        Submit registration info to create an account.
        """
        self.q(css='.js-login.login-button').first.click()
        time.sleep(60)
        #dashtest1=self.q(css='.js-login.login-button').visible
        #print(dashtest1)
        self.q(css='.js-login.login-button').first.click()

        # The next page is the dashboard; make sure it loads
        #dashboard = DashboardPageExtended(self.browser)
        #time.sleep(60)
        #dashboard.wait_for_page(90)
        
        return "http://edx.devstack.lms:18000/dashboard"
        #return dashboard

    def click_remember_me(self):
        """
        Clicks Remember Me checkbox
        """
        self.q(css='#login-remember').click()
        # Click initiates an ajax call
        self.wait_for_ajax()
