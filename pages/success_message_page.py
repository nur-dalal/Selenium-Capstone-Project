from base.base_page import BasePage
from selenium.webdriver.common.by import By

class SuccessMessagePage(BasePage):
    SUCCESS_MESSAGE_LOCATOR = (By.XPATH, '//*[@id="contact-page"]/div[2]/div[1]/div/div[2]')
    HOME_BTN_LOCATOR = (By.XPATH, '//*[@id="form-section"]/a/span')
    def visible_message_submitted(self):
        return self.find_web_element(self.SUCCESS_MESSAGE_LOCATOR).text
    
    def home_page_btn(self):
        self.click_operation(self.HOME_BTN_LOCATOR)
