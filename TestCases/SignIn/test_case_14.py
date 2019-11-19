import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class SignInTest14(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_14(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Click on hamburger icon
        signin.click_hamburger_icon()
        # Click on "Privacy statement" link
        signin.click_hamb_privacy_statement()
        time.sleep(1)
        # Switch to next window in browser
        signin.switch_next_window()
        # Verify if "Privacy statement" link was opened
        element = self.driver.find_element_by_xpath(SignIn.verify_privacy_stat)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest14"))
