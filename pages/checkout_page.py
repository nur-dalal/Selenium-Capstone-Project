from base.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    NAME_LOCATOR = (By.XPATH, '//*[@id="address_delivery"]/li[2]')
    CITY_LOCATOR = (By.XPATH, '//*[@id="address_delivery"]/li[5]')
    MOB_LOCATOR = (By.XPATH, '//*[@id="address_delivery"]/li[8]')
    REVIEW_ORDER_TEXT_LOCATOR = (By.XPATH, '//*[@id="cart_items"]/div/div[4]/h2')
    COMMENT_AREA_TEXT_FIELD_LOCATOR = ( By.XPATH, '//*[@id="ordermsg"]/textarea')
    PLACE_ORDER_BUTTON_LOCATOR = ( By.XPATH, '//*[@id="cart_items"]/div/div[7]/a')

    def check_address_details(self):
        name_text = self.find_web_element(self.NAME_LOCATOR).text
        city_text = self.find_web_element(self.CITY_LOCATOR).text
        mob_text = self.find_web_element(self.MOB_LOCATOR).text
        return name_text, city_text, mob_text
    
    def check_review_order(self):
        return self.find_web_element(self.REVIEW_ORDER_TEXT_LOCATOR).text
    
    def comment_area_text_field(self, message):
        self.enter_text(self.COMMENT_AREA_TEXT_FIELD_LOCATOR, message)
        self.click_operation(self.PLACE_ORDER_BUTTON_LOCATOR)
        print("'Place Order' submitted sucessfully")
    

