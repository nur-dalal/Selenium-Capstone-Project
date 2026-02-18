from base.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class ContactUsPage(BasePage):
    CONTACT_US_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a')
    GET_IN_US_LOCATOR = (By.XPATH, '//*[@id="contact-page"]/div[2]/div[1]/div/h2')
    NAME_LOCATOR = (By.XPATH, '//*[@id="contact-us-form"]/div[1]/input')
    EMAIL_LOCATOR = (By.XPATH, '//*[@id="contact-us-form"]/div[2]/input')
    SUBJECT_LOCATOR = (By.XPATH, '//*[@id="contact-us-form"]/div[3]/input')
    MESSAGE_LOCATOR = (By.XPATH, '//*[@id="message"]')
    CHOOSE_FILE_LOCATOR = (By.XPATH, '//*[@id="contact-us-form"]/div[5]/input')
    SUBMIT_LOCATOR = (By.XPATH, '//*[@id="contact-us-form"]/div[6]/input')
    

    def click_contact_us(self):
        self.click_operation(self.CONTACT_US_LOCATOR)
    
    def visible_get_in_touch(self):
        return self.find_web_element(self.GET_IN_US_LOCATOR).text
    
    def fill_details(self, name, email, subject, message):
        self.enter_text(self.NAME_LOCATOR, name)
        self.enter_text(self.EMAIL_LOCATOR, email)
        self.enter_text(self.SUBJECT_LOCATOR, subject)
        self.enter_text(self.MESSAGE_LOCATOR, message)
    
    def file_upladed(self, path):
        self.driver.find_element(*self.CHOOSE_FILE_LOCATOR).send_keys(path)

        print('file uploaded successfully!')

    def submit(self):
        self.click_operation(self.SUBMIT_LOCATOR)
        print('Message submitted successfully')
    