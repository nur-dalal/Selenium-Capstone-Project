import pytest, time
from pages.home_page import HomePage
from util.scroll_util import ScrollUtil

@pytest.mark.usefixtures('setup')
class TestCase10:
    def test_verify_subscription_in_home_page(self):
        try:
            # 3. Verify that home page is visible successfully
            hm_obj = HomePage(self.driver)
            hm_obj.home_page()
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print("Verified that home page is visible successfully")

            # 4. Scroll down to footer
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scrollTo_bottom()

            # 5. Verify text 'SUBSCRIPTION'
            subscription_test = hm_obj.visible_subscription_text()
            assert 'SUBSCRIPTION' in subscription_test
            print("Verify text 'SUBSCRIPTION'")

            # 6. Enter email address in input and click arrow button
            hm_obj.enter_email_address('nurdalal@gmail.com')

            # 7. Verify success message 'You have been successfully subscribed!' is visible
            alert_text = hm_obj.visible_success_alert()
            assert alert_text == 'You have been successfully subscribed!'
            print("Verify success message 'You have been successfully subscribed!' is visible")
        except Exception as e:
            print(e)

        # time.sleep(1)