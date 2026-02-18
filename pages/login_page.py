from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    SIGNUP_SIGNIN_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    LOGIN_TO_AC_VISIBLE_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/h2')
    EMAIL_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
    PASSWORD_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]')
    LOGIN_BTN_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button')
    LOGGED_AS_USERNAME_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    INCORRECT_USERID_PASSWORD_TEXT_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p')

    def click_signin_signup_btn(self):
        self.click_operation(self.SIGNUP_SIGNIN_LOCATOR)
    
    def visible_login_to_user_ac(self):
        return self.find_web_element(self.LOGIN_TO_AC_VISIBLE_LOCATOR).text
    
    def sign_in(self, email, password):
        self.enter_text(self.EMAIL_LOCATOR, email)
        self.enter_text(self.PASSWORD_LOCATOR, password)
        self.click_operation(self.LOGIN_BTN_LOCATOR)
        print("Login successful")
    
    def visible_logged_as_username(self):
        return self.find_web_element(self.LOGGED_AS_USERNAME_LOCATOR).text
    
    def visible_incorrect_id_pass(self):
        return self.find_web_element(self.INCORRECT_USERID_PASSWORD_TEXT_LOCATOR).text
    