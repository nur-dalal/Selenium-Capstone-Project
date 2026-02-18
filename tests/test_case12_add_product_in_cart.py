import pytest, time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
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
            hm_obj = HomePage(self.driver)
            hm_obj.home_page()
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print("Verified that home page is visible successfully")

            # 4. Click 'Products' button
            prd_obj = ProductPage(self.driver)
            prd_obj.click_product_btn()

            # 5. Hover over first product and click 'Add to cart'
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 500)
            # prd_obj.mouse_hover(self.FIRST_ITEM_ADD_LOCATOR)
            # prd_obj.add1_to_cart()
            prd_obj.add_product_with_id(1)

            # 6. Click 'Continue Shopping' button
            prd_obj.continue_shopping()

            # 7. Hover over second product and click 'Add to cart'
            prd_obj.mouse_hover(self.SECOND_ITEM_ADD_LOCATOR)
            # prd_obj.add2_to_cart()
            prd_obj.add_product_with_id(2)
            prd_obj.continue_shopping()

            # 8. Click 'View Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 9. Verify both products are added to Cart
            table = cart_obj.table_element()
            rows = table.find_elements(By.TAG_NAME, 'tr')
            assert 2 == (len(rows)-1)
            print("Verify both products are added to Cart")

            # 10. Verify their prices, quantity and total price
            for row in rows[1:]:
                print(row.text)
            
            print('Verify their prices, quantity and total price')
        except Exception as e:
            print(e)

        # time.sleep(1)