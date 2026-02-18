from base.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CART_PAGE_URL = 'https://www.automationexercise.com/view_cart'
    CHECKOUT_URL = 'https://www.automationexercise.com/checkout'

    CART_BTN_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')
    TABLE_LOCATOR = (By.ID, 'cart_info')
    QUANTITY_OF_PRODUCT = (By.XPATH, '//*[@id="product-1"]/td[4]/button')
    CHECKOUT_BTN_LOCATOR = (By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a')
    REGISTER_LOGIN_BTN_LOCATOR = (By.XPATH, '//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a/u')
    CONTINUE_ON_CART_LOCATOR = (By.XPATH, '//*[@id="checkoutModal"]/div/div/div[3]/button')
    REMOVE_PRDUCT1_LOCATOR = (By.XPATH, '//*[@id="product-1"]/td[6]/a')
    EMPTY_TEXT_LOCATOR = (By.CSS_SELECTOR, '#empty_cart')

    def click_cart_btn(self):
        self.click_operation(self.CART_BTN_LOCATOR)
    
    def no_rows_cart_table(self):
        table = self.find_web_element(self.TABLE_LOCATOR)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        return len(rows)
    
    def table_element(self):
        return self.find_web_element(self.TABLE_LOCATOR)
    
    def first_item_no_of_qty(self):
        return self.find_web_element(self.QUANTITY_OF_PRODUCT).text
    
    def click_checkout_btn(self):
        self.click_operation(self.CHECKOUT_BTN_LOCATOR)
    
    def click_register_login_btn(self):
        self.click_operation(self.REGISTER_LOGIN_BTN_LOCATOR)
    
    def click_continue_on_cart(self):
        self.click_operation(self.CONTINUE_ON_CART_LOCATOR)
    
    def remove_product_with_id(self, product_id):
        self.click_operation((By.XPATH, f'//*[@data-product-id="{product_id}"]'))
        print('Remove product successfully')
    
    def cart_is_empty(self):
        empty_text = self.find_web_element(self.EMPTY_TEXT_LOCATOR).text
        if 'empty' in empty_text:
            print('Verified that product is removed from the cart')