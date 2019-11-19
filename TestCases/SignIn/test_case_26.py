import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class SignInTest26(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholson@djimail.com"
    password = "87654321"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_26(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Enter a valid email account (jacknicholson@djimail.com)
        signin.set_email(self.email)
        # Click on "Next" button
        signin.click_next_button()
        time.sleep(1)
        # Enter an invalid password (87654321)
        signin.set_password(self.password)
        # Click "Sign in" button
        signin.click_password_signin_button()
        time.sleep(1)
        # Verify if an error message appeared (The email and password combination you entered doesn't match.)
        element = self.driver.find_element_by_xpath(SignIn.alert_message_2)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest26"))
