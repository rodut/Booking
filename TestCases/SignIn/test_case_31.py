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


class SignInTest31(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholson@djimail.com"
    password = "12345678"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_31(self):
        wait = WebDriverWait(self.driver, 10)
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Enter a valid email account (jacknicholson@djimail.com)
        signin.set_email(self.email)
        # Click on "Next" button
        signin.click_next_button()
        time.sleep(1)
        # Enter a valid password (12345678)
        signin.set_password(self.password)
        # Click "Sign in" button
        signin.click_password_signin_button()
        time.sleep(1)
        # Click back arrow (on browser)
        signin.window_back_page()
        # Go to booking.com
        time.sleep(1)
        self.driver.get(signin.url)
        # Click on "Your Account" dropdown menu
        signin.click_your_account()
        # Click on "My Dashboard" link
        signin.click_my_dashboard_link()
        # Verify if user is still logged in
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.verify_success_signin)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest31"))
