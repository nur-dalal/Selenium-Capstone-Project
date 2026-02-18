import pytest, time
from selenium.webdriver.common.by import By
from util.scroll_util import ScrollUtil
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from util.scroll_util import ScrollUtil
from pages.register_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.delete_page import DeletePage

@pytest.mark.usefixtures('setup')
class TestCase14:
    FIRST_ITEM_ADD_LOCATOR = (By.XPATH, '//html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a')
    def test_place_order_register_while_checkout(self):
        try:
            # 3. Verify that home page is visible successfully
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print("Verified that home page is visible successfully")

            # 4.  Add products to cart
            prd_obj = ProductPage(self.driver)
            prd_obj.click_product_btn()
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 500)
            # prd_obj.mouse_hover(self.FIRST_ITEM_ADD_LOCATOR)
            # prd_obj.add1_to_cart()
            prd_obj.add_product_with_id(2)
            prd_obj.continue_shopping()

            # 5. Click 'Cart' button
            scroll_obj.scrollTo_top()
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 6. Verify that cart page is displayed
            cart_title = self.driver.title
            assert 'Automation Exercise - Checkout' in cart_title
            print("Verify that cart page is displayed")

            # 7. Click Proceed To Checkout
            cart_obj.click_checkout_btn()

            # 8. Click 'Register / Login' button
            cart_obj.click_register_login_btn()

            # 9. Fill all details in Signup and create account
            signup_signin_obj = SignupLoginPage(self.driver)
            signup_signin_obj.signup_loginin_button()
            
            signup_signin_obj.signup('Nur', 'nurjd@wipro.com')
            enter_ac_info_text = signup_signin_obj.visible_enter_ac_info()
            assert enter_ac_info_text == 'ENTER ACCOUNT INFORMATION'
            print("Verify that 'ENTER ACCOUNT INFORMATION' is visible")

            ac_info_obj = AccountInfoPage(self.driver)
            ac_info_obj.account_detals('mr', 'nur@123', '1', 'November', '2001')

            ac_info_obj.check_box('newsletter')

            ac_info_obj.address_info('Nur','Dalal','Wipro','Taldangra', 'Bankura','India','WB','Bankura','722152',6294939500)

            ac_created_text = ac_info_obj.visible_account_created()

            # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
            assert ac_created_text == 'ACCOUNT CREATED!'
            print("Verify that 'ACCOUNT CREATED!' is visible")

            ac_info_obj.click_continue()

            # 11. Verify ' Logged in as username' at top
            logged_as_text = ac_info_obj.logged_as()
            print(logged_as_text)

            # 12. Click 'Cart' button
            cart_obj.click_cart_btn()

            # 13. Click 'Proceed To Checkout' button
            cart_obj.click_checkout_btn()

            # 14. Verify Address Details and Review Your Order
            checkout_obj = CheckoutPage(self.driver)
            name_text, city_text, mob_text = checkout_obj.check_address_details()
            review_text = checkout_obj.check_review_order()

            if 'Nur' in name_text and 'Bankura' in city_text and "6294939500" in mob_text:
                print("Verify Address Details")
            
            if 'Review Your Order' in review_text:
                print('Verified Review Your Order')
            
            # 15. Enter description in comment text area and click 'Place Order'
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scrollTo_bottom()

            checkout_obj.comment_area_text_field('This is my oreder')

            # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
            pay_obj = PaymentPage(self.driver)
            pay_obj.payment_details('Digital Inidia Card', '6267 7452 3214 5531', '345', '11', '2030')

            # 17. Click 'Pay and Confirm Order' button
            # 18. Verify success message 'Congratulations! Your order has been confirmed!'
            pay_obj.pay_n_confirm()

            # 19. Click 'Delete Account' button
            del_obj = DeletePage(self.driver)
            del_obj.delete_account()

            # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
            del_ac_text = del_obj.visible_ac_deleted()
            assert del_ac_text == 'ACCOUNT DELETED!'
            print("Verify that 'ACCOUNT DELETED!' is visible")
            del_obj.click_continue()
        except Exception as e:
            print(e)

        # time.sleep(1)