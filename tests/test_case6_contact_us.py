from pages.contact_us_page import ContactUsPage
from util.allert_util import AlertUtil
from pages.success_message_page import SuccessMessagePage
from util.scroll_util import ScrollUtil
import pytest, time, os

@pytest.mark.usefixtures('setup')
class TestCase6:
    def test_contact_us(self):
        try:
            # 3. Verify that home page is visible successfully
            title = self.driver.title
            assert title == 'Automation Exercise'
            print('Verify that home page is visible successfully')

            # 4. Click on 'Contact Us' button
            cn_obj = ContactUsPage(self.driver)
            cn_obj.click_contact_us()

            # 5. Verify 'GET IN TOUCH' is visible
            get_in_touch_text = cn_obj.visible_get_in_touch()
            assert get_in_touch_text == "GET IN TOUCH"
            print("Verify 'GET IN TOUCH' is visible")

            # 6. Enter name, email, subject and message
            scroll_obj = ScrollUtil(self.driver)
            scroll_obj.scroll_by(0, 200)
            cn_obj.fill_details('Nur','nurdalal@gmail.com','Subject to subject', 'This is message')

            # 7. Upload file

            file_path = os.path.abspath("tests/testfile.txt") 
            cn_obj.file_upladed(file_path)

            # 8. Click 'Submit' button
            cn_obj.submit()

            # 9. Click OK button
            alert_obj = AlertUtil(self.driver)
            alert_obj.accept_alert()

            # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
            sc_obj = SuccessMessagePage(self.driver)
            success_mesaage_text = sc_obj.visible_message_submitted()
            assert 'Success! Your details have been submitted successfully.' in success_mesaage_text
            print("Verify success message 'Success! Your details have been submitted successfully.' is visible")

            # 11. Click 'Home' button and verify that landed to home page successfully
            sc_obj.home_page_btn()
            title = self.driver.title
            assert 'Automation Exercise' in title
            print("The landed to home page successfully")
        
        except Exception as e:
            print(e)

        # time.sleep(1)