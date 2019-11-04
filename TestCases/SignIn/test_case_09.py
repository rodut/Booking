import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class SignInTest09(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_09(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Click on hamburger icon
        signin.click_hamburger_icon()
        # Verify if hamburger icon contains "Create your account"
        element = self.driver.find_element_by_xpath(SignIn.hamburger_icon_1)
        assert element.is_displayed()
        # Verify if hamburger icon contains "Having trouble signing in"
        element = self.driver.find_element_by_xpath(SignIn.hamburger_icon_2)
        assert element.is_displayed()
        # Verify if hamburger icon contains "Privacy statement"
        element = self.driver.find_element_by_xpath(SignIn.hamburger_icon_3)
        assert element.is_displayed()
        # Verify if hamburger icon contains "Terms & conditions"
        element = self.driver.find_element_by_xpath(SignIn.hamburger_icon_4)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest09"))
