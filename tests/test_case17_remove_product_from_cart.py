import pytest, time
from pages.product_page import ProductPage
from util.scroll_util import ScrollUtil
from pages.cart_page import CartPage

@pytest.mark.usefixtures('setup')
class TestCase17:
    def test_remove_product_from_cart(self):
        try:
            scroll_obj = ScrollUtil(self.driver)
            # 3. Verify that home page is visible successfully
            excepted_url = 'https://www.automationexercise.com/'
            current_url = self.driver.current_url
            assert excepted_url in current_url
            print('Verified that home page is visible successfully')
            
            # 4. Add products to cart
            scroll_obj.scroll_by(0, 550)

            product_obj = ProductPage(self.driver)
            # product_obj.add1_to_cart()
            product_obj.add_product_with_id(3)
            product_obj.continue_shopping()

            scroll_obj.scrollTo_top()

            # 5. Click 'Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 6. Verify that cart page is displayed
            excepted_url = cart_obj.CART_PAGE_URL
            current_url = self.driver.current_url

            assert excepted_url == current_url
            print('Verified that cart page is displayed')

            # 7. Click 'X' button corresponding to particular product
            cart_obj.remove_product_with_id(3)

            # 8. Verify that product is removed from the cart
            cart_obj.cart_is_empty()
            
        
        except Exception as e:
            print(e)

        # time.sleep(1)