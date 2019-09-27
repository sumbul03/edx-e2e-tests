from edxapp_acceptance.pages.lms.dashboard import DashboardPage


class AccountPage(DashboardPage):
      """ 
      Account Settings Page
      """
      url = None

      def user_account(self):
          """
          Clicks Drop down then Account Setting
          """
          self.q(css='.kt-header__topbar-user').click()
          self.wait_for_element_visibility(
            '.kt-notification__item[href="/account/settings"] .kt-notification__item-details .kt-notification__item-title', 'Account'
        )
          self.q(css='.kt-notification__item[href="/account/settings"]').click()
      
      def is_browser_on_page(self):
          return self.q(css='h3.kt-subheader__title')[0].text == 'Account Settings'
      
     
      def click_order_history(self):
          self.q(css='#orders-tab]').click()
          print(self.q(css='button#orders-tab')[0].text== 'Order History')
          return self.q(css='button#orders-tab')[0].text 

      def click_linked_accounts(self):
          self.q(css='button#accounts-tab').click()
          print(self.q(css='button#accounts-tab')[0].text== 'Linked Accounts')
          return self.q(css='button#accounts-tab')[0].text 



