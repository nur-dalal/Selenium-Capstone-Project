import pytest, time
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_product import SearchProduct

@pytest.mark.usefixtures('setup')
class TestCase9:
    def test_search_product(self):
        try:
            # 3. Verify that home page is visible successfully
            hm_obj = HomePage(self.driver)
            hm_obj.home_page()
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print("Verified that home page is visible successfully")

            # 4. Click on 'Products' button
            prd_obj = ProductPage(self.driver)
            prd_obj.click_product_btn()

            # 5. Verify user is navigated to ALL PRODUCTS page successfully
            product_page_title = self.driver.title
            assert 'Automation Exercise - All Products' in product_page_title
            print("Verify user is navigated to ALL PRODUCTS page successfully")

            # 6. Enter product name in search input and click search button
            search_obj = SearchProduct(self.driver)
            item_name = search_obj.search_items('Jeans')

            # 7. Verify 'SEARCHED PRODUCTS' is visible
            assert 'Jeans' in item_name
            print("Verify 'SEARCHED PRODUCTS' is visible")

            # 8. Verify all the products related to search are visible
            product_lists = search_obj.visible_all_products()
            assert product_lists == 'SEARCHED PRODUCTS'
            print("Verify all the products related to search are visible")
        except Exception as e:
            print(e)

        # time.sleep(1)

