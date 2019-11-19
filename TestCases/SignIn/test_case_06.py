import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class SignInTest06(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_06(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Click on "Privacy Statement" link
        signin.click_privacy_statement_link()
        # Switch to next window in browser
        signin.switch_next_window()
        # Verify if "Privacy Statement" link was opened
        element = self.driver.find_element_by_xpath(SignIn.verify_privacy_stat)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest06"))
