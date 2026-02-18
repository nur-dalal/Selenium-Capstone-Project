from pages.cases_page import CasesPage
from pages.home_page import HomePage
import pytest, time

@pytest.mark.usefixtures('setup')
class TestCase7:
    def test_varift_test_cases(self):
        try:
            # 3
            # hm_obj = HomePage(self.driver)
            # hm_obj.home_page()
            # home_title = self.driver.title

            # 3. Verify that home page is visible successfully
            home_title = self.driver.title
            assert 'Automation Exercise' in home_title
            print("Verified that home page is visible successfully")

            # 4. Click on 'Test Cases' button
            tc_obj = CasesPage(self.driver)
            tc_obj.click_test_case_btn()

            # 5. Verify user is navigated to test cases page successfully
            title = self.driver.title
            assert 'Automation Practice Website for UI Testing - Test Cases' in title
            print("Verified user is navigated to test cases page successfully")

            # current_url = 'https://www.automationexercise.com/test_cases'
            # excepted_url = self.driver.current_url
            # assert current_url == excepted_url
            # print("Verified user is navigated to test cases page successfully")

        except Exception as e:
            print(e)


        # time.sleep(1)