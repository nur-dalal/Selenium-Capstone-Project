import pytest, time
from util.scroll_util import ScrollUtil
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
@pytest.mark.usefixtures('setup')
class TestCase22:
    def test_add_to_cart_from_recommended_items(self):
        try:
            # 3. Scroll to bottom of page
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scrollTo_bottom()
            home_obj = HomePage(self.driver)

            # 4. Verify 'RECOMMENDED ITEMS' are visible
            recommended_items_text = home_obj.visiable_recommended_items()
            assert 'RECOMMENDED ITEMS' in recommended_items_text
            print("Verify 'RECOMMENDED ITEMS' are visible")

            # 5. Click on 'Add To Cart' on Recommended product
            product_obj = ProductPage(self.driver)
            product_ids_from_recommended_items = [4, 5, 6]
            for id in product_ids_from_recommended_items:
                product_obj.click_operation(('xpath', f'//a[@data-product-id="{id}"]'))
                product_obj.continue_shopping()
            
            # 6. Click on 'View Cart' button
            cart_obj = CartPage(self.driver)
            cart_obj.click_cart_btn()

            # 7. Verify that product is displayed in cart page
            all_jeans_present = 0
            for id in product_ids_from_recommended_items:
                element = product_obj.find_web_element(('xpath', f'//a[@data-product-id="{id}"]'))
                if element.is_displayed():
                    product_name = product_obj.find_web_element(('xpath', f'//a[@href="/product_details/{id}"]')).text
                    print(f'{product_name} is present')
                    all_jeans_present += 1
            if all_jeans_present == len(product_ids_from_recommended_items):
                print('Verify that product is displayed in cart page')
            else:
                print('Not Verified')

        except Exception as e:
            print(e)
        
        # time.sleep(1)