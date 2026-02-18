import pytest, time
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures('setup')
class TestCase11:
    def test_verify_subscription_in_cart(self):
        try:
            # 3. Verify that home page is visible successfully
            hm_obj = HomePage(self.driver)
            hm_obj.home_page()
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print("Verified that home page is visible successfully")

            # 4. Click 'Cart' button and scroll down to footer
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

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
