import pytest, time
from util.scroll_util import ScrollUtil
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('setup')
class TestCase26:
    def test_verify_scrollUp_without_arrow_button_and_scroll_down_functionality(self):
        try:
            # 3. Verify that home page is visible successfully
            expected_url = 'https://www.automationexercise.com/'
            current_url = self.driver.current_url
            assert expected_url == current_url
            print("Verify that home page is visible successfully")

            # 4. Scroll down page to bottom
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scrollTo_bottom()

            # 5. Verify 'SUBSCRIPTION' is visible
            home_obj = HomePage(self.driver)
            subscription_text = home_obj.visible_subscription_text()
            assert 'SUBSCRIPTION' in subscription_text
            print("Verify 'SUBSCRIPTION' is visible")

            # 6. Scroll up page to top
            scroll_obj.scrollTo_top()

            # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
            text = home_obj.find_web_element((By.XPATH, '//*[@id="slider-carousel"]/div/div[1]/div[1]/h2')).text
            assert 'Full-Fledged practice website for Automation Engineers' in text
            print("Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen")
            print(text)

        except Exception as e:
            print(e)
        
        # time.sleep(1)