"""
Student logout page.
"""
from edxapp_acceptance.pages.lms.dashboard import DashboardPage
from regression.pages.lms.login_lms import LmsLogin
from bok_choy .promise import BrokenPromise
from regression.pages.lms import LOGIN_BASE_URL

class MainPage(LmsLogin):
    url = "http://edx.devstack.lms:18000" 

    def is_browser_on_page(self):
        return self.q(css='.parallax-img').present # check for element on that page


class DashboardLogout(DashboardPage):
    """
    This class is an extended class of Dashboard Page,
    where we add methods that are different or not used in DashboardPage
    """
    url = 'http://edx.devstack.lms:18000' + '/dashboard'

    def logout_lms(self):
        """
        Clicks Drop down then SignOut button
        """
        self.q(css='.kt-header__topbar-user').click()
        self.wait_for_element_visibility(
            '.kt-notification__custom a[href="/logout"]', 'Sign Out'
        )
        self.q(css='.kt-notification__custom a[href="/logout"]').click()
