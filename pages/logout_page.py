from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LogoutPage(BasePage):
    LOGOUT_BTN_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')

    def logout(self):
        self.click_operation(self.LOGOUT_BTN_LOCATOR)
        print('Logout successfully!')