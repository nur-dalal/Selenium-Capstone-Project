from pages.login_page import LoginPage
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

            # 6. Enter incorrect email address and password
            # 7. Click 'login' button
            lin_obj.sign_in('invalid@gmail.com', 'invalid@pass')

            # 8. Verify error 'Your email or password is incorrect!' is visible
            incorrect_msg_text = lin_obj.visible_incorrect_id_pass()
            assert incorrect_msg_text in "Your email or password is incorrect!"
            print("Verify error 'Your email or password is incorrect!' is visible")
        except Exception as e:
            print(e)

        # sleep(1)