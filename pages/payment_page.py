from base.base_page import BasePage
from selenium.webdriver.common.by import By
from util.scroll_util import ScrollUtil

class PaymentPage(BasePage):
    NAME_ON_CART_LOCATOR = (By.XPATH, '//*[@id="payment-form"]/div[1]/div/input')
    CARD_NO_LOCATOR = (By.XPATH, '//*[@id="payment-form"]/div[2]/div/input')
    CVV_TEXT_FIELD_AREA_LOCATOR = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/input')
    EXPIRATION_MONTH_LOCATOR = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[2]/input')
    EXPIRATION_YEAR_LOCATOR = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[3]/input')
    PAY_N_CONFIRM_BTN_LOCATOR = (By.XPATH, '//*[@id="submit"]')

    CONGRATS_TEXT_LOCATOR = (By.XPATH, '//*[@id="form"]/div/div/div/p')

    def scroll_by_100(self, x=0, y=100):
        scroll_obj = ScrollUtil(self.driver)
        scroll_obj.scroll_by(x, y)
    
    def payment_details(self, card_name, card_no, cvv, expiration_month, expiration_year):
        self.scroll_by_100()
        self.enter_text(self.NAME_ON_CART_LOCATOR, card_name)
        self.enter_text(self.CARD_NO_LOCATOR, card_no)
        self.enter_text(self.CVV_TEXT_FIELD_AREA_LOCATOR, cvv)
        self.enter_text(self.EXPIRATION_MONTH_LOCATOR, expiration_month)
        self.enter_text(self.EXPIRATION_YEAR_LOCATOR, expiration_year)

    def pay_n_confirm(self):
        self.click_operation(self.PAY_N_CONFIRM_BTN_LOCATOR)
        print("Payment details submitted successfully")

        congrats_text = self.find_web_element(self.CONGRATS_TEXT_LOCATOR).text

        if "Congratulations! Your order has been confirmed!" in congrats_text:
            print("Verified success message 'Congratulations! Your order has been confirmed!'")
        else:
            print("Order not successfull")
        
            

