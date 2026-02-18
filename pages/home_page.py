from base.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    HOME_PAGE_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[1]/a')
    SUBSCRIPTION_TEXT_LOCATOR = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[2]/div/h2')
    EMAIL_ADDRESS_LOCATOR = (By.XPATH, '//*[@id="susbscribe_email"]')
    EMAIL_ADDRESS_BTN_LOCATOR = (By.XPATH, '//*[@id="subscribe"]')
    SUCCESS_ALERT_LOCATOR = (By.CSS_SELECTOR, '#success-subscribe > div')
    RECOMMENDED_ITEMS_TEXT_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div[2]/h2')

    def home_page(self):
        self.click_operation(self.HOME_PAGE_LOCATOR)
    
    def visible_subscription_text(self):
        return self.find_web_element(self.SUBSCRIPTION_TEXT_LOCATOR).text
    
    def enter_email_address(self, email):
        self.enter_text(self.EMAIL_ADDRESS_LOCATOR, email)
        self.click_operation(self.EMAIL_ADDRESS_BTN_LOCATOR)
    
    def visible_success_alert(self):
        return self.find_web_element(self.SUCCESS_ALERT_LOCATOR).text
    
    def visiable_recommended_items(self):
        return self.find_web_element(self.RECOMMENDED_ITEMS_TEXT_LOCATOR).text