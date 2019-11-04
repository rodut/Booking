import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class SignInTest24(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholso44n@djimail.com"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_24(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Enter an invalid email
        signin.set_email(self.email)
        # Click on "Next" button
        signin.click_next_button()
        time.sleep(1)
        # Verify if an alert message appeared
        element = self.driver.find_element_by_xpath(SignIn.alert_message_1)
        assert element.is_displayed()
        # Click on "create an account" link
        signin.click_create_acc_link()
        # Verify if the form changed to "Create your account"
        element = self.driver.find_element_by_xpath(SignIn.verify_signup_page)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest24"))
