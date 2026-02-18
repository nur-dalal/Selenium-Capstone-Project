from pages.product_page import ProductPage
import pytest, time

@pytest.mark.usefixtures('setup')
class TestCase8:
    def test_varify_all_product(self):
        try:
            # 3. Verify that home page is visible successfully
            title = self.driver.title
            assert 'Automation Exercise' in title
            print("Verified that home page is visible successfully")

            # 4. Click on 'Products' button
            prd_obj = ProductPage(self.driver)
            prd_obj.click_product_btn()

            # 5. Verify user is navigated to ALL PRODUCTS page successfully
            product_page_title = self.driver.title
            assert 'Automation Exercise - All Products' in product_page_title
            print("Verify user is navigated to ALL PRODUCTS page successfully")

            # 6. The products list is visible
            all_product_list = prd_obj.visible_all_product()
            assert 'ALL PRODUCTS' in all_product_list 
            print("The products list is visible")

            # 7. Click on 'View Product' of first product
            prd_obj.first_products_view()

            # 8. User is landed to product detail page
            title = self.driver.title
            assert 'Automation Exercise - Product Details' in title
            print('User is landed to product detail page')

            # 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
            name, category, price, availability, condition, brand = prd_obj.visible_products_details()
            if name and category and price and availability and condition and brand:
                print("Verified that detail detail is visible: product name, category, price, availability, condition, brand")
        except Exception as e:
            print(e)

        # time.sleep(1)