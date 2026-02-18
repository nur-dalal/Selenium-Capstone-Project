import pytest, time
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from util.scroll_util import ScrollUtil
from pages.cart_page import CartPage
from pages.login_page import LoginPage

@pytest.mark.usefixtures('setup')
class TestCase20:
    def test_search_products_verify_cart_after_pogin(self):
        try:
            scroll_obj = ScrollUtil(self.driver)
            # 3. Click on 'Products' button
            product_obj = ProductPage(self.driver)
            product_obj.click_product_btn()

            # 4. Verify user is navigated to ALL PRODUCTS page successfully
            all_product_visible_text = product_obj.visible_all_product()
            assert 'ALL PRODUCTS' in all_product_visible_text
            print("Verify user is navigated to ALL PRODUCTS page successfully")

            # 5. Enter product name in search input and click search button
            product_obj.search_product_with_name('Jeans')
            product_obj.searching_product_btn()

            # 6. Verify 'SEARCHED PRODUCTS' is visible
            search_product_text = product_obj.visiable_search_product_text()
            assert 'SEARCHED PRODUCTS' in search_product_text
            print("Verify 'SEARCHED PRODUCTS' is visible")

            # 7. Verify all the products related to search are visible
            jeans_all_search_product_text = product_obj.visiable_jeans_all_search_product()

            if 'Regular Fit Straight Jeans' in jeans_all_search_product_text and 'Soft Stretch Jeans' in jeans_all_search_product_text and 'Grunt Blue Slim Fit Jeans' in jeans_all_search_product_text:
                print("Verify all the products related to search are visible")
            else:
                print('Search products missing')
            
            # 8. Add those products to cart
            scroll_obj.scroll_by(0, 500)
            jeans_product_id = [33, 35, 37]
            for id in jeans_product_id:
                product_obj.add_product_with_id(id)
                product_obj.continue_shopping()
            
            # 9. Click 'Cart' button and verify that products are visible in cart
            scroll_obj.scrollTo_top()
            cart_obj = CartPage(self.driver) 
            cart_obj.click_cart_btn()
            scroll_obj.scroll_by(0, 200)
        
            all_jeans_present = 0
            for id in jeans_product_id:
                element = product_obj.find_web_element(('xpath', f'//a[@data-product-id="{id}"]'))
                if element.is_displayed():
                    product_name = product_obj.find_web_element(('xpath', f'//a[@href="/product_details/{id}"]')).text
                    print(f'{product_name} is present')
                    all_jeans_present += 1
            if all_jeans_present == len(jeans_product_id):
                print('Verify all the products related to search are visible')
            else:
                print('Not Verify all the products related to search are visible')
            
            # 10. Click 'Signup / Login' button and submit login details
            login_obj = LoginPage(self.driver)
            login_obj.click_signin_signup_btn()
            login_obj.sign_in('nurdalal@gmail.com', 'nur@123')

            # 11. Again, go to Cart page
            time.sleep(0.5)
            cart_obj.click_cart_btn()
            scroll_obj.scroll_by(0, 200)
        
            # 12. Verify that those products are visible in cart after login as well
            all_jeans_present = 0
            for id in jeans_product_id:
                element = product_obj.find_web_element(('xpath', f'//a[@data-product-id="{id}"]'))
                if element.is_displayed():
                    product_name = product_obj.find_web_element(('xpath', f'//a[@href="/product_details/{id}"]')).text
                    print(f'{product_name} is present')
                    all_jeans_present += 1
            if all_jeans_present == len(jeans_product_id):
                print('Verify that those products are visible in cart after login as well')
            else:
                print('Not Verify all the products related to search are visible')
            
            # 13. Remove all products that have been added
            for id in jeans_product_id:
                time.sleep(0.5)
                product_obj.click_operation(('xpath', f'//a[@data-product-id="{id}"]'))
                all_jeans_present -= 1
            if all_jeans_present == 0:
                print('Remove all products that have been added')

            # 14. Verify 'Cart is empty! Click here to buy products.' is visible
            cart_obj.cart_is_empty()

        except Exception as e:
            print(e)

        # time.sleep(1)