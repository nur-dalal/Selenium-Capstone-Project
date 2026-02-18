import pytest
from time import sleep
from pages.login_page import LoginPage

@pytest.mark.usefixtures('setup')
class TestCase2:
    def test_login_user(self):
        try:
            # 3. Verify that home page is visible successfully
            title = self.driver.title
            assert title == 'Automation Exercise'
            print('Verify that home page is visible successfully')
            login_obj = LoginPage(self.driver)

            # 4. Click on 'Signup / Login' button
            login_obj.click_signin_signup_btn()

            # 5. Verify 'Login to your account' is visible
            visible_text = login_obj.visible_login_to_user_ac()
            assert visible_text == 'Login to your account'
            print("Verified 'Login to your account' is visible")

            # 6. Enter correct email address and password
            # 7. Click 'login' button
            login_obj.sign_in('nurdalal@gmail.com', 'nur@123')

            # 8. Verify that 'Logged in as username' is visible
            username_visible_text = login_obj.visible_logged_as_username()
            assert username_visible_text == 'Logged in as Nur'
            print(f"Verify that '{username_visible_text}' is visible")
        
        except Exception as e:
            print(e)

        # sleep(1)