import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class SignInTest21(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_21(self):
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Verify if "By signing in or creating an account, you agree with our" text is present
        element = self.driver.find_element_by_xpath(SignIn.verify_create_acc_agree_text)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest21"))
