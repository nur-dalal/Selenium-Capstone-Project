from base.base_page import BasePage
from selenium.webdriver.common.by import By

class DeletePage(BasePage):
    DELETE_BUTTON_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    ACCOUNT_DELETED_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div/div/a')

    def delete_account(self):
        self.click_operation(self.DELETE_BUTTON_LOCATOR)
    
    def visible_ac_deleted(self):
        return self.find_web_element(self.ACCOUNT_DELETED_LOCATOR).text
    
    def click_continue(self):
        self.click_operation(self.CONTINUE_BUTTON_LOCATOR)
        print('Continue....')
