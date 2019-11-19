import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class SignInTest08(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_08(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Select "Deutsch" language
        element = self.driver.find_element_by_xpath(SignIn.select_lang_de)
        dropdown = Select(element)
        dropdown.select_by_value("de")
        time.sleep(1)
        # Verify if the language of the page was changed to Deutsch
        element = self.driver.find_element_by_xpath(SignIn.verify_lang_de)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest08"))
