from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from time import sleep
import pytest
@pytest.mark.usefixtures('setup')
class TestCase3:
    def test_login_with_incoreect_id_pass(self):
        try:
            # 3. Verify that home page is visible successfully
            title = self.driver.title
            assert "Automation Exercise" in title
            print("Verify that home page is visible successfully")

            # 4. Click on 'Signup / Login' button
            lin_obj = LoginPage(self.driver)
            lin_obj.click_signin_signup_btn()

            # 5. Verify 'Login to your account' is visible
            visible_login_text = lin_obj.visible_login_to_user_ac()
            assert visible_login_text == 'Login to your account'
            print("Verify 'Login to your account' is visible")

            # 6. Enter correct email address and password
            # 7. Click 'login' button
            lin_obj.sign_in('nurdalal@gmail.com', 'nur@123')

            # 8. Verify that 'Logged in as username' is visible
            logged_in_username_text = lin_obj.visible_logged_as_username()
            assert "Logged in as Nur" in logged_in_username_text
            print("Verify that 'Logged in as Nur' is visible")

            # 9. Click 'Logout' button
            lout_obj = LogoutPage(self.driver)
            lout_obj.logout()

            #10. Verify that user is navigated to login page
            current_title = self.driver.title
            assert 'Automation Exercise - Signup / Login' in current_title
            print("Verify that user is navigated to login page")

        except Exception as e:
            print(e)
        
        # sleep(1)
