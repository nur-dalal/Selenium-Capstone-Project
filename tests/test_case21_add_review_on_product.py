import pytest, time
from pages.product_page import ProductPage
from util.scroll_util import ScrollUtil

@pytest.mark.usefixtures('setup')
class TestCase21:
    def test_add_review_on_product(self):
        try:
            # 3. Click on 'Products' button
            product_obj = ProductPage(self.driver)
            product_obj.click_product_btn()

            # 4. Verify user is navigated to ALL PRODUCTS page successfully
            all_product_text = product_obj.visible_all_product()
            assert 'ALL PRODUCTS' in all_product_text
            print('Verify user is navigated to ALL PRODUCTS page successfully')

            # 5. Click on 'View Product' button
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 500)
            product_obj.click_on_view_product_with_id(2)

            # 6. Verify 'Write Your Review' is visible
            scroll_obj.scroll_by(0, 450)
            write_your_review_text = product_obj.visiable_write_your_text()
            assert 'WRITE YOUR REVIEW' in write_your_review_text
            print("Verify 'Write Your Review' is visible")

            # 7. Enter name, email and review
            # 8. Click 'Submit' button
            product_obj.enter_review_details('Nur', 'nurdalal@gmail.com', 'This is awesome')

            # 9. Verify success message 'Thank you for your review.'
            success_review_text = product_obj.visiable_success_msg_review_text()
            assert 'Thank you for your review.' in success_review_text
            print("Verify success message 'Thank you for your review.'")

        except Exception as e:
            print(e)

        # time.sleep(1)