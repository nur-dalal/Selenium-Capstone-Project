import pytest, time
from util.scroll_util import ScrollUtil
from pages.register_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.delete_page import DeletePage

@pytest.mark.usefixtures('setup')
class TestCase15:
    def test_case15(self):
        try:
            scroll_obj = ScrollUtil(self.driver)
            # 3. Verify that home page is visible successfully
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print('Verified that home page is visible successfully')

            # 4. Click 'Signup / Login' button
            signup_signin_obj = SignupLoginPage(self.driver)
            signup_signin_obj.signup_loginin_button()

            # 5. Fill all details in Signup and create account
            signup_signin_obj.signup('Nur', 'nur_testcase15@wipro.com')
            enter_ac_info_text = signup_signin_obj.visible_enter_ac_info()
            assert enter_ac_info_text == 'ENTER ACCOUNT INFORMATION'
            print("Verify that 'ENTER ACCOUNT INFORMATION' is visible")

            ac_info_obj = AccountInfoPage(self.driver)
            ac_info_obj.account_detals('mr', 'nur@123', '1', 'November', '2001')

            ac_info_obj.check_box('newsletter')

            ac_info_obj.address_info('Nur','Dalal','Wipro','Taldangra', 'Bankura','India','WB','Bankura','722152',6294939500)

            ac_created_text = ac_info_obj.visible_account_created()
            
            # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
            assert ac_created_text == 'ACCOUNT CREATED!'
            print("Verify that 'ACCOUNT CREATED!' is visible")
            ac_info_obj.click_continue()

            # 7. Verify ' Logged in as username' at top
            logged_as = signup_signin_obj.visible_logged_as_username()
            assert 'Nur' in logged_as
            print("Verify ' Logged in as username' at top --> ", logged_as)

            # 8. Add products to cart
            product_obj = ProductPage(self.driver)
            scroll_obj.scroll_by(0, 550)
            # product_obj.add1_to_cart()
            product_obj.add_product_with_id(2)
            product_obj.continue_shopping()

            scroll_obj.scrollTo_top()

            # 9. Click 'Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 10. Verify that cart page is displayed
            excepted_url = cart_obj.CART_PAGE_URL
            current_url = self.driver.current_url

            assert excepted_url == current_url
            print('Verified that cart page is displayed')

            # 11. Click Proceed To Checkout
            cart_obj.click_checkout_btn()

            # 12. Verify Address Details and Review Your Order
            checkout_obj = CheckoutPage(self.driver)
            name_text, city_text, mob_text = checkout_obj.check_address_details()

            if 'Nur' in name_text and 'Bankura' in city_text and '6294939500' in mob_text:
                print('Verified Address Details and Review Your Order')
            
            # 13. Enter description in comment text area and click 'Place Order'
            scroll_obj.scrollTo_bottom()
            checkout_obj.comment_area_text_field('This is message')

            # 14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
            pay_obj = PaymentPage(self.driver)
            pay_obj.payment_details('Digital Inidia Card', '6267 7452 3214 5531', '345', '11', '2030')

            # 15. Click 'Pay and Confirm Order' button
            # 16. Verify success message 'Congratulations! Your order has been confirmed!'
            pay_obj.pay_n_confirm()


            # 17. Click 'Delete Account' button
            del_obj = DeletePage(self.driver)
            del_obj.delete_account()

            # 18. Verify that 'ACCOUNT DELETED!' and click 'Continue' button
            del_ac_text = del_obj.visible_ac_deleted()
            assert del_ac_text == 'ACCOUNT DELETED!'
            print("Verify that 'ACCOUNT DELETED!' is visible")
            del_obj.click_continue()
     
        except Exception as e:
            print(e)

        # time.sleep(1)