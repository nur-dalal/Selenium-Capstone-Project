from base.base_page import BasePage
from util.scroll_util import ScrollUtil
from selenium.webdriver.common.by import By
from time import sleep

class AccountInfoPage(BasePage):
    TITLE_MR_BUTTON_LOCATOR = (By.XPATH, '//*[@id="id_gender1"]')
    TITLE_MRS_BUTTON_LOCATOR = (By.XPATH, '//*[@id="id_gender2"]')
    PASSWORD_LOCATOR = (By.XPATH, '//*[@id="password"]')
    DAY_LOCATOR = (By.XPATH, '//*[@id="days"]')
    MONTH_LOCATOR = (By.XPATH, '//*[@id="months"]')
    YEAR_LOCATOR = (By.XPATH, '//*[@id="years"]')
    CHECKBOX_NEWSLETTER_LOCATOR = (By.XPATH, '//*[@id="newsletter"]')
    CHECKBOX_PARTNER_LOCATOR = (By.XPATH, '//*[@id="optin"]')

    FIRST_NAME_LOCATOR = (By.XPATH, '//*[@id="first_name"]')
    LAST_NAME_LOCATOR = (By.XPATH, '//*[@id="last_name"]')
    COMPANY_NAME_LOCATOR = (By.XPATH, '//*[@id="company"]')
    ADDRESS1_LOCATOR = (By.XPATH, '//*[@id="address1"]')
    ADDRESS2_LOCATOR = (By.XPATH, '//*[@id="address2"]')
    COUNTRY_LOCATOR = (By.XPATH, '//*[@id="country"]')
    STATE_LOCATOR = (By.XPATH, '//*[@id="state"]')
    CITY_LOCATOR = (By.XPATH, '//*[@id="city"]')
    ZIPCODE_LOCATOR = (By.XPATH, '//*[@id="zipcode"]')
    MOB_NUM_LOCATOR = (By.XPATH, '//*[@id="mobile_number"]')
    CREATE_ACC_BUTTON = (By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button')
    ACCOUNT_CREATED_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    CONTINUE_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div/div/a')
    LOGGED_AS_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    DELETE_AC_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')


    def account_detals(self, title, password, d, m, y):
        sc_obj = ScrollUtil(self.driver)
        sc_obj.scroll_by(0, 200)
        if title.lower() == 'mr':
            self.click_operation(self.TITLE_MR_BUTTON_LOCATOR)
        else:
            self.click_operation(self.TITLE_MRS_BUTTON_LOCATOR)
         
        self.enter_text(self.PASSWORD_LOCATOR, password)

        self.enter_text(self.DAY_LOCATOR, d)
        self.enter_text(self.MONTH_LOCATOR, m)
        self.enter_text(self.YEAR_LOCATOR, y)
        print('Details submission successfull')
    
    def check_box(self, check):
        sc_obj = ScrollUtil(self.driver)
        sc_obj.scroll_by(0, 400)
        if check.lower() == 'partners':
            self.click_operation(self.CHECKBOX_PARTNER_LOCATOR)
            print("'Receive special offers from our partners!'")
        else:
            self.click_operation(self.CHECKBOX_NEWSLETTER_LOCATOR)
            print("'Sign up for our newsletter!")
    
    def address_info(self, fname, lname, cname, add1, add2, country, state, city, zipcode, mob):
        sc_obj = ScrollUtil(self.driver)
        sc_obj.scroll_by(0, 200)
        self.enter_text(self.FIRST_NAME_LOCATOR, fname)
        # sleep(2)
        self.enter_text(self.LAST_NAME_LOCATOR, lname)
        self.enter_text(self.COMPANY_NAME_LOCATOR, cname)
        self.enter_text(self.ADDRESS1_LOCATOR, add1)
        self.enter_text(self.ADDRESS2_LOCATOR, add2)
        self.enter_text(self.COUNTRY_LOCATOR, country)

        sc_obj.scroll_by(0, 350)

        self.enter_text(self.STATE_LOCATOR, state)
        self.enter_text(self.CITY_LOCATOR, city)
        self.enter_text(self.ZIPCODE_LOCATOR, zipcode)
        self.enter_text(self.MOB_NUM_LOCATOR, mob)
        self.click_operation(self.CREATE_ACC_BUTTON)
        print('Address information submitted successfully')
        
    def visible_account_created(self):
        return self.find_web_element(self.ACCOUNT_CREATED_LOCATOR).text
    
    def click_continue(self):
        self.click_operation(self.CONTINUE_LOCATOR)

    def logged_as(self):
        return self.find_web_element(self.LOGGED_AS_LOCATOR).text

    def delete_ac(self):
        self.click_operation(self.DELETE_AC_LOCATOR)
