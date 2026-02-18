from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CategoryBarPage(BasePage):
    LEFT_CATEGORY_BAR_LOCATOR = (By.XPATH, '/html/body/section[2]/div/div/div[1]/div')
    CLICK_ON_WOMEN_CATEGORY_LOCATOR = (By.XPATH, '//*[@id="accordian"]/div[1]/div[1]/h4/a')
    CLICK_ON_WOMEN_DRESS_SUBCATEGORY_LOCATOR = (By.XPATH, '//*[@id="Women"]/div/ul/li[1]/a')
    CLICK_ON_WOMEN_TOPS_SUBCATEGORY_LOCATOR = (By.XPATH, '//*[@id="Women"]/div/ul/li[2]/a')
    CLICK_ON_WOMEN_SAREE_SUBCATEGORY_LOCATOR = (By.XPATH, '//*[@id="Women"]/div/ul/li[3]/a')

    CLICK_ON_MEN_CATEGORY_LOCATOR = (By.XPATH, '//*[@id="accordian"]/div[2]/div[1]/h4/a') 
    CLICK_ON_MEN_TSHIRT_SUBCATEGORY_LOCATOR = (By.XPATH, '//*[@id="Men"]/div/ul/li[1]/a')
    CLICK_ON_MEN_JEANS_SUBCATEGORY_LOCATOR = (By.XPATH, '//*[@id="Men"]/div/ul/li[2]/a')

    CLICK_ON_KIDS_CATEGORY_LOCATOR = (By.XPATH, '//*[@id="accordian"]/div[3]/div[1]/h4/a')

    WOMEN_DRESS_PRODUCT_TEXT_LOCATOR = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/h2')
    MEN_DRESS_PRODUCT_TEXT_LOCATOR = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/h2')

    def visible_left_category_bar(self):
        left_category_bar = self.find_web_element(self.LEFT_CATEGORY_BAR_LOCATOR).text
        # print(left_category_bar)
        if 'WOMEN' in left_category_bar and 'MEN' in left_category_bar and 'KIDS' in left_category_bar:
            print('Verify that categories are visible on left side bar')
        else:
            print('Not')
    
    def click_women_category(self, sub_category='dress'):
        self.click_operation(self.CLICK_ON_WOMEN_CATEGORY_LOCATOR)

        if sub_category.lower() == 'dress':
            self.click_operation(self.CLICK_ON_WOMEN_DRESS_SUBCATEGORY_LOCATOR)
        elif sub_category.lower() == 'tops':
            self.click_operation(self.CLICK_ON_WOMEN_TOPS_SUBCATEGORY_LOCATOR)
        else:
            self.click_operation(self.CLICK_ON_WOMEN_SAREE_SUBCATEGORY_LOCATOR)
    
    def visible_women_dress_product(self):
        return self.find_web_element(self.WOMEN_DRESS_PRODUCT_TEXT_LOCATOR).text
    
    def visible_men_dress_product(self):
        return self.find_web_element(self.MEN_DRESS_PRODUCT_TEXT_LOCATOR).text
    
    def click_men_category(self, sub_category='tshirt'):
        self.click_operation(self.CLICK_ON_MEN_CATEGORY_LOCATOR)

        if sub_category.lower() == 'tshirt':
            self.click_operation(self.CLICK_ON_MEN_TSHIRT_SUBCATEGORY_LOCATOR)
        else:
            self.click_operation(self.CLICK_ON_MEN_JEANS_SUBCATEGORY_LOCATOR)
    

        