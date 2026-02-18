from base.base_page import BasePage
from util.scroll_util import ScrollUtil
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    PRODUCT_BTN_LOCATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
    ALL_PRODUCT_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/h2')
    BLUE_TOP_PRODUCT_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a')
    MEN_TSHIRT_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[2]/ul/li/a')

    ADD1_TO_CART_BTN_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a')
    ADD2_TO_CART_BTN_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a')
    CONTINUE_SHOPPING_BTN_LOCATOR = (By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button')


    PRODUCT_NAME_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2')
    CATEGORY_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]')
    PRICE_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span')
    ADD_QTY_LOCATOR = (By.XPATH, '//*[@id="quantity"]')
    CLICK_ADD_TO_CART_BTN_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')
    AVAILABILITY_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]/b')
    CONDITION_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]/b')
    BRAND_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]/b')

    BRANDS_BAR_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[1]/div/div[3]')
    BRAND_PAGE_TEXT_LOCATOR = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/h2')

    SEARCH_FIELD_LOCATOR = (By.XPATH, '//*[@id="search_product"]')
    SEARCH_BTN_LOCATOR = (By.XPATH, '//*[@id="submit_search"]')
    SEARCH_PRODUCT_TEXT = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/h2')

    JEANS_ALL_SEARCH_PRODUCT_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div')

    WRITE_YOUR_REVIEW_TEXT_LOCATOR = (By.XPATH, '/html/body/section/div/div/div[2]/div[3]/div[1]/ul/li/a')



    def click_product_btn(self):
        self.click_operation(self.PRODUCT_BTN_LOCATOR)
        print('Product button is clicked')
    
    def visible_all_product(self):
        return self.find_web_element(self.ALL_PRODUCT_LOCATOR).text
    
    def add1_to_cart(self):
        self.click_operation(self.ADD1_TO_CART_BTN_LOCATOR)
    
    def add_product_with_id(self, product_id):
        self.click_operation((By.XPATH, f'//a[@data-product-id="{product_id}"]'))
    
    def add2_to_cart(self):
        self.click_operation(self.ADD2_TO_CART_BTN_LOCATOR)
    
    def add_qty_of_product(self, num):
        self.remove_enter_text(self.ADD_QTY_LOCATOR, num)
    
    def click_add_to_cart_btn(self):
        self.click_operation(self.CLICK_ADD_TO_CART_BTN_LOCATOR)

    def continue_shopping(self):
        self.click_operation(self.CONTINUE_SHOPPING_BTN_LOCATOR)
    
    def first_products_view(self):
        sc_obj = ScrollUtil(self.driver)
        sc_obj.scroll_by(0, 450)
        self.click_operation(self.BLUE_TOP_PRODUCT_LOCATOR)
        print("'View Product' of first product")
    
    def second_products_view(self):
        sc_obj = ScrollUtil(self.driver)
        sc_obj.scroll_by(0, 450)
        self.click_operation(self.MEN_TSHIRT_LOCATOR)
        print("'View Product' of first product")
    
    def view_product_name(self):
        return self.find_web_element(self.PRODUCT_NAME_LOCATOR).text
    def view_product_category(self):
        return self.find_web_element(self.CATEGORY_LOCATOR).text
    def view_product_price(self):
        return self.find_web_element(self.PRICE_LOCATOR).text
    def view_product_availability(self):
        return self.find_web_element(self.AVAILABILITY_LOCATOR).text
    def view_product_condition(self):
        return self.find_web_element(self.CONDITION_LOCATOR).text
    def view_product_brand(self):
        return self.find_web_element(self.BRAND_LOCATOR).text
    
    def visible_products_details(self):
        name = self.view_product_name()
        category = self.view_product_category()
        price = self.view_product_price()
        availability = self.view_product_availability()
        condition = self.view_product_condition()
        brand = self.view_product_brand()
        return name, category, price, availability, condition, brand
    
    def visible_brands_bar(self):
        return self.find_web_element(self.BRANDS_BAR_LOCATOR).text
    
    def click_on_brand_name_with_id(self, brand_id=1):
        self.click_operation((By.CSS_SELECTOR, f'body > section:nth-child(3) > div > div > div.col-sm-3 > div > div.brands_products > div > ul > li:nth-child({brand_id}) > a'))

    def visible_brand_text_locator(self):
        return self.find_web_element(self.BRAND_PAGE_TEXT_LOCATOR).text
    
    def search_product_with_name(self, pname='Jeans'):
        sc_obj = ScrollUtil(self.driver)
        sc_obj.scroll_by(0, 400)
        self.enter_text(self.SEARCH_FIELD_LOCATOR, pname)
    
    def searching_product_btn(self):
        self.click_operation(self.SEARCH_BTN_LOCATOR)

    def visiable_search_product_text(self):
        return self.find_web_element(self.SEARCH_PRODUCT_TEXT).text
    
    def visiable_jeans_all_search_product(self):
        return self.find_web_element(self.JEANS_ALL_SEARCH_PRODUCT_LOCATOR).text
    
    def add_all_jeans_products(self, product_id):
        self.click_operation((By.XPATH, f"//a[@data-product-id='{product_id}']"))
    
    def click_on_view_product_with_id(self, product_id):
        self.click_operation((By.XPATH, f'//a[@href="/product_details/{product_id}"]'))
    
    def visiable_write_your_text(self):
        return self.find_web_element(self.WRITE_YOUR_REVIEW_TEXT_LOCATOR).text
    
    def enter_review_details(self, name, email, add_review):
        self.enter_text((By.XPATH, '//*[@id="name"]'), name)
        self.enter_text((By.XPATH, '//*[@id="email"]'), email)
        self.enter_text((By.XPATH, '//*[@id="review"]'), add_review)
        print('Enter name, email and review added successfully')

        self.click_operation((By.XPATH, '//*[@id="button-review"]'))
    
    def visiable_success_msg_review_text(self):
            return self.find_web_element((By.XPATH, '//*[@id="review-section"]/div/div/span')).text