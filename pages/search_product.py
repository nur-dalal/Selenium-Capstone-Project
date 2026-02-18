from base.base_page import BasePage
from util.scroll_util import ScrollUtil
from selenium.webdriver.common.by import By

class SearchProduct(BasePage):
    SEACH_FIELD_LOCATOR = (By.XPATH, '//*[@id="search_product"]')
    SEARCH_BTN_LOCATOR = (By.XPATH, '//*[@id="submit_search"]')
    SEACH_ITEM_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/p')
    SEARCH_LIST_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/h2')

    def search_items(self, item):
        sc_obj = ScrollUtil(self.driver)
        sc_obj.scroll_by(0, 550)

        self.enter_text(self.SEACH_FIELD_LOCATOR, item)
        self.click_operation(self.SEARCH_BTN_LOCATOR)
        print('Searching done')

        sc_obj.scroll_by(0, 400)

        return self.find_web_element(self.SEACH_ITEM_LOCATOR).text
    
    def visible_all_products(self):
        return self.find_web_element(self.SEARCH_LIST_LOCATOR).text

