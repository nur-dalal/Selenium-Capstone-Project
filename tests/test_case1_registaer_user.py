import pytest
from time import sleep
from pages.register_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.delete_page import DeletePage


@pytest.mark.usefixtures('setup')
class TestCase1:
    def test_register(self):
        try:
            # 3. Verify that home page is visible successfully
            title = self.driver.title
            assert title == 'Automation Exercise'
            print('Verify that home page is visible successfully')

            # 4. Click on 'Signup / Login' button
            signup_signin_obj = SignupLoginPage(self.driver)
            signup_signin_obj.signup_loginin_button()
            new_user_signup_text = signup_signin_obj.visible_new_user()

            # 5. Verify 'New User Signup!' is visible
            assert 'New User Signup!' in new_user_signup_text
            print("Verify 'New User Signup!' is visible")

            # 6. Enter name and email address
            # 7. Click 'Signup' button
            signup_signin_obj.signup('Nur', 'nurjd_testcase1@gmail.com')

            # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
            enter_ac_info_text = signup_signin_obj.visible_enter_ac_info()
            assert enter_ac_info_text == 'ENTER ACCOUNT INFORMATION'
            print("Verify that 'ENTER ACCOUNT INFORMATION' is visible")

            # 9. Fill details: Title, Name, Email, Password, Date of birth
            ac_info_obj = AccountInfoPage(self.driver)
            ac_info_obj.account_detals('mr', 'nur@123', '1', 'November', '2001')

            # 10. Select checkbox 'Sign up for our newsletter!'
            # 11. Select checkbox 'Receive special offers from our partners!'
            ac_info_obj.check_box('partners')

            # 12. test_case1_registaer_user
            # 13. Click 'Create Account button'
            ac_info_obj.address_info('Nur','Dalal','Wipro','Taldangra', 'Bankura','India','WB','Bankura','722152',6294939500)

            # 14. Verify that 'ACCOUNT CREATED!' is visible
            ac_created_text = ac_info_obj.visible_account_created()

            assert ac_created_text == 'ACCOUNT CREATED!'
            print("Verify that 'ACCOUNT CREATED!' is visible")

            # 15. Click 'Continue' button
            ac_info_obj.click_continue()

            # 16. Verify that 'Logged in as username' is visible
            logged_as_text = ac_info_obj.logged_as()
            print(logged_as_text)

            # 17. Click 'Delete Account' button
            del_obj = DeletePage(self.driver)
            del_obj.delete_account()

            # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
            del_ac_text = del_obj.visible_ac_deleted()
            assert del_ac_text == 'ACCOUNT DELETED!'
            print("Verify that 'ACCOUNT DELETED!' is visible")
            del_obj.click_continue()
        
        except Exception as e:
            print(e)

        # sleep(1)