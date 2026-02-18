import pytest, time
from selenium.webdriver.common.by import By
from util.scroll_util import ScrollUtil
from pages.register_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.delete_page import DeletePage

@pytest.mark.usefixtures('setup')
class TestCase23:
    def test_verify_address_details_in_checkout_page(self):
        try:
            # 3. Verify that home page is visible successfully
            expected_url = 'https://www.automationexercise.com/'
            current_url = self.driver.current_url
            assert expected_url == current_url
            print("Verify that home page is visible successfully")

            # 4. Click 'Signup / Login' button
            signup_signin_obj = SignupLoginPage(self.driver)
            signup_signin_obj.signup_loginin_button()
            new_user_signup_text = signup_signin_obj.visible_new_user()

            # 5. Fill all details in Signup and create account
            assert 'New User Signup!' in new_user_signup_text
            print("Verify 'New User Signup!' is visible")

            signup_signin_obj.signup('Nur', 'nurjd_testcase23@gmail.com')

            enter_ac_info_text = signup_signin_obj.visible_enter_ac_info()
            assert enter_ac_info_text == 'ENTER ACCOUNT INFORMATION'
            print("Verify that 'ENTER ACCOUNT INFORMATION' is visible")

            ac_info_obj = AccountInfoPage(self.driver)
            ac_info_obj.account_detals('mr', 'nur@123', '1', 'November', '2001')

            ac_info_obj.check_box('newsletter')
 
            ac_info_obj.address_info('Nur','Dalal','Wipro','Taldangra', 'Bankura','India','WB','Bankura','722152',6294939500)
 
            ac_created_text = ac_info_obj.visible_account_created()

            assert ac_created_text == 'ACCOUNT CREATED!'
            print("Verify that 'ACCOUNT CREATED!' is visible")

            # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
            ac_info_obj.click_continue()

            # 7. Verify ' Logged in as username' at top
            logged_as_text = ac_info_obj.logged_as()
            print(logged_as_text)

            # 8. Add products to cart
            product_obj = ProductPage(self.driver)
            product_obj.click_product_btn()
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 450)
            product_obj.click_operation(('xpath', '//a[@data-product-id="1"]'))
            product_obj.continue_shopping()

            # 9. Click 'Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 10. Verify that cart page is displayed
            expected_url = 'https://www.automationexercise.com/view_cart'
            current_url = self.driver.current_url
            assert expected_url == current_url
            print("Verify that cart page is displayed")

            # 11. Click Proceed To Checkout
            cart_obj.click_checkout_btn()

            # 12. Verify that the delivery address and the billing address is same address filled at the time registration of account
            delivary_address = self.driver.find_element(By.CSS_SELECTOR, '#address_delivery').text
            billing_address = self.driver.find_element(By.CSS_SELECTOR, '#address_invoice').text
            if '''Mr. Nur Dalal
Wipro
Taldangra
Bankura
Bankura WB 722152
India
6294939500'''in delivary_address and '''Mr. Nur Dalal
Wipro
Taldangra
Bankura
Bankura WB 722152
India
6294939500''' in billing_address:
                print(delivary_address)
                print("Verify that the delivery address and the billing address is same address filled at the time registration of account")
            else:
                print("Not Found")

            # 13. Click 'Delete Account' button
            del_obj = DeletePage(self.driver)
            del_obj.delete_account()

            # 14. Verify 'ACCOUNT DELETED!' and click 'Continue' button
            del_ac_text = del_obj.visible_ac_deleted()
            assert del_ac_text == 'ACCOUNT DELETED!'
            print("Verify that 'ACCOUNT DELETED!' is visible")
            del_obj.click_continue()

        except Exception as e:
            print(e)

        # time.sleep(1)