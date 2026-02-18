import pytest, time
from pages.product_page import ProductPage
from util.scroll_util import ScrollUtil

@pytest.mark.usefixtures('setup')
class TestCase19:
    def test_view_and_cart_brand_products(self):
        try:
            # 3. Click on 'Products' button
            product_obj = ProductPage(self.driver)
            product_obj.click_product_btn()

            #4. Verify that Brands are visible on left side bar
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 450)

            # 5. Click on any brand name
            product_obj.click_on_brand_name_with_id(brand_id=1)

            # 6. Verify that user is navigated to brand page and brand products are displayed
            polo_brand_text = product_obj.visible_brand_text_locator()
            assert 'POLO' in polo_brand_text
            print(polo_brand_text)
            print("Verify that user is navigated to brand page and brand products are displayed")

            # 7. On left side bar, click on any other brand link
            self.driver.back()
            scroll_obj.scroll_by(0, 200)
            product_obj.click_on_brand_name_with_id(brand_id=2)

            hnm_brand_text = product_obj.visible_brand_text_locator()
            
            # 8. Verify that user is navigated to that brand page and can see products
            assert 'H&M' in hnm_brand_text
            print(hnm_brand_text)
            print("Verify that user is navigated to that brand page and can see products")
        
        except Exception as e:
            print(e)

        # time.sleep(1)