import pytest
from time import sleep
from pages.register_page import SignupLoginPage


@pytest.mark.usefixtures('setup')
class TestCase5:
    def test_register_with_exsisting_email(self):
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

            # 6. Enter name and already registered email address
            # 7. Click 'Signup' button
            signup_signin_obj.signup('Nur', 'nurdalal@gmail.com')

            # 8. Verify error 'Email Address already exist!' is visible
            email_already_exist_text = signup_signin_obj.visible_email_already_exist()
            assert 'Email Address already exist!' in email_already_exist_text
            print("Verify error 'Email Address already exist!' is visible")

        except Exception as e:
            print(e)
        
        # sleep(1)
