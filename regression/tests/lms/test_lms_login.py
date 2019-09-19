"""
End to end tests for LMS Login
"""
import os
import time
from bok_choy.web_app_test import WebAppTest
from regression.pages.lms.login_lms import LmsLogin
from regression.pages.lms.dashboard_lms import DashboardPageExtended
from regression.pages.lms import LMS_BASE_URL, LMS_STAGE_BASE_URL


class LoginTest(WebAppTest):
    """
    Tests for logging in and navigating to Courseware page
    """

    #DEMO_COURSE_USER = os.environ.get('USER_LOGIN_EMAIL')
    #DEMO_COURSE_PASSWORD = os.environ.get('USER_LOGIN_PASSWORD')
    DEMO_COURSE_USER = "staff@example.com"
    DEMO_COURSE_PASSWORD = "edx"

    def setUp(self):
        """
        Initialize the page object
        """
        super(LoginTest, self).setUp()
        self.login_page = LmsLogin(self.browser)
        self.dashboard_ext = DashboardPageExtended(self.browser)

    def test_login(self):
        """
        Verifies that user can Log in as a staff
        """
        self.login_page.visit()
        time.sleep(45)
        self.login_page.login(self.DEMO_COURSE_USER, self.DEMO_COURSE_PASSWORD)
        time.sleep(45)
        print(self.q(css='.message-copy')[0].text)
        all_co = self.login_page.q(
                css='.my-courses').present
        print(all_co)
        
        self.assertEqual(
            all_co,True,
            msg='User not logged in as expected.') 
        
    def atest_remember_me(self):
        """
        Verifies that user can use Remember Me functionality
        """
        cookie_name = 'stage-edx-sessionid'

        if LMS_STAGE_BASE_URL != LMS_BASE_URL:
            cookie_name = 'sessionid'

        self.login_page.visit()
        self.login_page.provide_info(
            self.DEMO_COURSE_USER, self.DEMO_COURSE_PASSWORD
        )

        self.login_page.click_remember_me()
        self.login_page.submit()
        self.dashboard_ext.wait_for_page()
        # When we check the 'remember me' checkbox
        # then edx keeps the session alive for 7 days.
        # In which case, cookie has 'expiry' value of
        # 7 days. If we don't check the 'remember me'
        # then the value of 'expiry' key of cookie will
        # be none.
        self.assertIsNotNone(self.browser.get_cookie(cookie_name)['expiry'])
