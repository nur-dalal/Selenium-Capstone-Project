import pytest, time
from pages.category_bar_page import CategoryBarPage
from util.scroll_util import ScrollUtil

@pytest.mark.usefixtures('setup')
class TestCase18:
    def test_view_category_product(self):
        try:
            # 3. Verify that categories are visible on left side bar
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 400)
            category_obj = CategoryBarPage(self.driver)
            category_obj.visible_left_category_bar()

            # 4. Click on 'Women' category
            # 5. Click on any category link under 'Women' category, for example: Dress
            category_obj.click_women_category('dress')

            # 6. Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'
            women_dress_text = category_obj.visible_women_dress_product()
            if 'WOMEN' in women_dress_text:
                print("Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'")
            else:
                print("Not valid")

            # 7. On left side bar, click on any sub-category link of 'Men' category
            category_obj.click_men_category('jeans')
            men_dress_text = category_obj.visible_men_dress_product()
            if 'MEN' in men_dress_text:
                print("Verify that category page is displayed and confirm text 'MEN - JEANS PRODUCTS'")
            else:
                print("Not valid")
            
            # 8. Verify that user is navigated to that category page
            expected_url = 'https://www.automationexercise.com/category_products/6'
            current_url = self.driver.current_url
            assert expected_url == current_url
            print('Verified that user is navigated to that category page')
        except Exception as e:
            print(e)

        # time.sleep(1)