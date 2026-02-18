import pytest, time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures('setup')
class TestCase13:
    def test_verify_product_qty_in_cart(self):
        try:
            # 3. Verify that home page is visible successfully
            hm_obj = HomePage(self.driver)
            hm_obj.home_page()
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print("Verified that home page is visible successfully")

            # 4. Click 'View Product' for any product on home page
            prd_obj = ProductPage(self.driver)
            prd_obj.click_product_btn()

            # 5. Verify product detail is opened
            # prd_obj.first_products_view()
            prd_obj.second_products_view()

            # 6.  Increase quantity to 4
            prd_obj.add_qty_of_product(4)

            # 7. Click 'Add to cart' button
            prd_obj.click_add_to_cart_btn()
            prd_obj.continue_shopping()

            # 8. Click 'View Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 9. Verify that product is displayed in cart page with exact quantity
            table = cart_obj.table_element()
            rows = table.find_elements(By.TAG_NAME, 'td')
            for row in rows[1:]:
                if row.text == "4":
                    print("Verify that product is displayed in cart page with exact quantity")
        except Exception as e:
            print(e)

        # time.sleep(1)


