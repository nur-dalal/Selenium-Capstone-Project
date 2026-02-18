import pytest, time
from util.scroll_util import ScrollUtil
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

@pytest.mark.usefixtures('setup')
class TestCase16:
    def test_case16(self):
        try:
            scroll_obj = ScrollUtil(self.driver)
            # 3. Verify that home page is visible successfully
            title = self.driver.title
            assert title == 'Automation Exercise'
            print('Verify that home page is visible successfully')

            # 4. Click 'Signup / Login' button
            login_obj = LoginPage(self.driver)
            login_obj.click_signin_signup_btn()
            visible_text = login_obj.visible_login_to_user_ac()
            assert visible_text == 'Login to your account'
            print("Verified 'Login to your account' is visible")

            # 5. Fill email, password and click 'Login' button
            login_obj.sign_in('nurdalal@gmail.com', 'nur@123')

            # 6. Verify 'Logged in as username' at top
            logged_as = login_obj.visible_logged_as_username()
            assert 'Nur' in logged_as
            print("Verify ' Logged in as username' at top --> ", logged_as)

            # 7. Add products to cart
            scroll_obj.scroll_by(0, 550)

            product_obj = ProductPage(self.driver)
            # product_obj.add1_to_cart()
            product_obj.add_product_with_id(2)
            product_obj.continue_shopping()

            scroll_obj.scrollTo_top()

            # 8. Click 'Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 9. Verify that cart page is displayed
            excepted_url = cart_obj.CART_PAGE_URL
            current_url = self.driver.current_url

            assert excepted_url == current_url
            print('Verified that cart page is displayed')

            # 10. Click Proceed To Checkout
            cart_obj.click_checkout_btn()

            # 11. Verify Address Details and Review Your Order
            checkout_obj = CheckoutPage(self.driver)
            name_text, city_text, mob_text = checkout_obj.check_address_details()

            if 'Nur' in name_text and 'Bankura' in city_text and '6294939500' in mob_text:
                print('Verified Address Details and Review Your Order')
            
            # 12. Enter description in comment text area and click 'Place Order'
            scroll_obj.scrollTo_bottom()
            checkout_obj.comment_area_text_field('This is message')

            # 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
            pay_obj = PaymentPage(self.driver)
            pay_obj.payment_details('Digital Inidia Card', '6267 7452 3214 5531', '345', '11', '2030')

            # 14. Click 'Pay and Confirm Order' button
            # 15. Verify success message 'Congratulations! Your order has been confirmed!'
            pay_obj.pay_n_confirm()
     
        except Exception as e:
            print(e)

        # time.sleep(1)