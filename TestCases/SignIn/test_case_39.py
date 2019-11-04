import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class SignInTest39(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholson44@djimail.com"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_39(self):
        wait = WebDriverWait(self.driver, 10)
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Click on hamburger icon
        signin.click_hamburger_icon()
        time.sleep(1)
        # Select "Having trouble signing in?"
        signin.click_hamburger_icon_2()
        time.sleep(1)
        # Enter a invalid email address (jacknicholson44@djimail.com)
        signin.set_forgot_email(self.email)
        # Click on "Confirm" button
        signin.click_confirm_button()
        # Verify if an error message appears (Looks like there isn't an account associated with this email address...)
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.forgot_email_error)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest39"))
