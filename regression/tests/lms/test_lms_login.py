"""
End to end tests for LMS Login
"""
import os
import time
from bok_choy.web_app_test import WebAppTest
from regression.pages.lms.login_lms import LmsLogin
from regression.pages.lms.dashboard_lms import DashboardPageExtended
from regression.pages.lms.dashboard_lms import StartCourse
from regression.pages.lms.logout import DashboardLogout
from regression.pages.lms.logout import MainPage
from regression.pages.lms.account_setting import AccountPage
from regression.pages.lms.lms_courseware import CoursewarePageExtended
from regression.pages.lms import LMS_BASE_URL, LMS_STAGE_BASE_URL
from edxapp_acceptance.pages.lms.dashboard import DashboardPage



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
        self.dashboard_logout = DashboardLogout(self.browser)
        self.main = MainPage(self.browser)
        self.dashboard_page = DashboardPage(self.browser)
        #self.courseware_page = CoursewarePageExtended(self.browser, self.course_id)
        self.start_course = StartCourse(self.browser)
        self.account_setting = AccountPage(self.browser)

        self.login_page.visit()
        self.login_page.login(self.DEMO_COURSE_USER, self.DEMO_COURSE_PASSWORD)
               
    def test_at_main(self):
        """
        Verifies that user is on the main page
        """
        
        return self.main.q(css='.parallax-img').visible

    def test_login(self):
        """
        Verifies that user can Log in as a staff
        """
        
        all_co = self.login_page.q(
                css='#my-courses').visible
        print(all_co)

        self.assertEqual(
            all_co,True,
            msg='User not logged in as expected.')  

    def test_dashboard_course_listings(self):
        """
        Perform a general validation of the course listings section
        """
        
        self.dashboard_ext.visit()
        course_listings = self.dashboard_ext.get_course_listings()
        msg = len(course_listings)
        print(msg)

        self.assertEqual(len(course_listings), 1)
   
    def test_person_on_course_page(self):
        """
        View the Demo Course
        """
        self.dashboard_ext.q(css='.btn-label-brand.btn.btn-wide.btn-bold').first.click()
        check = self.dashboard_ext.q(
                css='h3.kt-portlet__head-title').visible
        print(check)
        self.assertEqual(
            check,
            True,
            msg='User not on Course Page.')
        
        self.start_course.q(css='.btn.btn-primary.action-resume-course').click()
        print('TEST')
         
    def test_start_course(self):
        """
        Start the Demo Course
        """
        self.dashboard_ext.q(css='.btn-label-brand.btn.btn-wide.btn-bold').first.click()
        
        self.start_course.q(css='.btn.btn-primary.action-resume-course').first.click()

        stc = self.start_course.q(
                css='#sequence-list').visible
              
        self.assertEqual(
            stc,
            True,
            msg='User not on Courseware Page.')
   
    def test_user_on_courseware_page(self):
        """
        Check if there is a side header with subsections
        """
        self.dashboard_ext.q(css='.btn-label-brand.btn.btn-wide.btn-bold').first.click()
        
        self.start_course.q(css='.btn.btn-primary.action-resume-course').first.click()
        
        return self.start_course.q(css='.kt-menu__subnav .kt-menu__item').present

    def test_logout(self):
        """
        Verifies that user can Log out
        """
        
        return self.dashboard_logout.q(css='.parallax-img').present

    def test_account(self):
        """
        Verifies that user can go to account's page
        """
        
        return self.account_setting.q(css='#about-tab').present


        
