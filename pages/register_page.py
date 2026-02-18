from base.base_page import BasePage
from selenium.webdriver.common.by import By
class SignupLoginPage(BasePage):

    SIGNUP_SIGNIN_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    NEW_USER_SIGNUP_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/h2')
    NAME_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
    EMAIL_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    SIGNUP_BUTTON_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button')

    ENTER_AC_INFO_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div/div[1]/h2/b')
    EMAIL_ALREADY_EXSIST_TEXT_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/p')

    LOGGED_AS_USERNAME_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')

    def signup_loginin_button(self):
        self.click_operation(self.SIGNUP_SIGNIN_LOCATOR)
        print("'Signup / Login' button is clicked")

    def visible_new_user(self):
        return self.find_web_element(self.NEW_USER_SIGNUP_LOCATOR).text
    
    def signup(self, name, email):
        self.enter_text(self.NAME_LOCATOR, name)
        self.enter_text(self.EMAIL_LOCATOR, email)
        self.click_operation(self.SIGNUP_BUTTON_LOCATOR)
    
    def visible_enter_ac_info(self):
        return self.find_web_element(self.ENTER_AC_INFO_LOCATOR).text
    
    def visible_email_already_exist(self):
        return self.find_web_element(self.EMAIL_ALREADY_EXSIST_TEXT_LOCATOR).text
    
    def visible_logged_as_username(self):
        return self.find_web_element(self.LOGGED_AS_USERNAME_LOCATOR).text