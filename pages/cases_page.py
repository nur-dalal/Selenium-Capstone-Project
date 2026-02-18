from base.base_page import BasePage
from selenium.webdriver.common.by import By

class CasesPage(BasePage):
    TEST_CASES_BTN_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')

    def click_test_case_btn(self):
        self.click_operation(self.TEST_CASES_BTN_LOCATOR)