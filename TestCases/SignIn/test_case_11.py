import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class SignInTest11(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_11(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Click on hamburger icon
        signin.click_hamburger_icon()
        # Click on "Create your account" link
        signin.click_hamburger_icon_1()
        time.sleep(1)
        # Verify if the form changed to "Create your account"
        element = self.driver.find_element_by_xpath(SignIn.verify_hamb_icon_1)
        assert element.is_displayed()
        # Click back arrow (on browser)
        signin.window_back_page()
        time.sleep(1)
        # Verify if the form changed to "Sign in"
        element = self.driver.find_element_by_xpath(SignIn.verify_signin)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest11"))
