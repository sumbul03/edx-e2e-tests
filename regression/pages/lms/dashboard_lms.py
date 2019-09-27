"""
Student dashboard page.
"""
from edxapp_acceptance.pages.lms.dashboard import DashboardPage
from bok_choy .promise import BrokenPromise
from regression.pages.lms import LOGIN_BASE_URL


class DashboardPageExtended(DashboardPage):
    """
    This class is an extended class of Dashboard Page,
    where we add methods that are different or not used in DashboardPage
    """
    url = 'http://edx.devstack.lms:18000' + '/dashboard'

    def is_browser_on_page(self):
        """
        Verifies if the browser is on the correct page
        """
        return self.q(css='#my-courses').visible

   

class StartCourse(DashboardPage):

    url = 'http://edx.devstack.lms:18000' + '/courses' + '/course-v1:edX+DemoX+Demo_Course' + '/course/' 

    def is_browser_on_page(self):
        return self.q(css='h3.kt-portlet__head-titles').present 

