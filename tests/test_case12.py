import pytest, time
from selenium.webdriver.common.by import By
from util.scroll_util import ScrollUtil
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures('setup')
class TestCase12:
    FIRST_ITEM_ADD_LOCATOR = (By.XPATH, '//html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a')
    SECOND_ITEM_ADD_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a')
    def test_verify_subscription_in_cart(self):
        try:
            # 3. Verify that home page is visible successfully
            title = self.driver.title
            assert 'Automation Exercise' in title
            print("Verify that home page is visible successfully")

            # 4. Click 'Products' button
            product_obj = ProductPage(self.driver)
            product_obj.click_product_btn()

            # 5. Hover over first product and click 'Add to cart'
            # 6. Click 'Continue Shopping' button
            # 7. Hover over second product and click 'Add to cart'
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 450)

            for id in range(1, 3):
                # product_obj.mouse_hover((By.XPATH, f'//a[@data-product-id="{id}"]'))
                product_obj.add_product_with_id(id)
                product_obj.continue_shopping()
                
            
            # 8. Click 'View Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 9. Verify both products are added to Cart
            table_contents = cart_obj.find_web_element((By.XPATH, '//*[@id="cart_info_table"]')).text
            if '''Item Description Price Quantity Total
    Blue Top
    Women > Tops
    Rs. 500
    1
    Rs. 500
    Men Tshirt
    Men > Tshirts
    Rs. 400
    1
    Rs. 400''' in table_contents:
                print("Verify both products are added to Cart")
            
            # 10. Verify their prices, quantity and total price
            assert "Rs. 500" in table_contents and "Rs. 400" in table_contents
            print("Verify their prices, quantity and total price")
        
        except Exception as e:
            print(e)

        # time.sleep(1)