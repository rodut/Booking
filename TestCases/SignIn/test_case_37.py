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


class SignInTest37(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholson@djimail.com"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_37(self):
        wait = WebDriverWait(self.driver, 10)
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Enter a valid email address (jacknicholson@djimail.com)
        signin.set_email(self.email)
        time.sleep(1)
        # Click "Sign up" link
        signin.click_signup_link()
        time.sleep(1)
        # Click back arrow (next to Booking.com Account)
        signin.click_back_arrow()
        # Verify if the email field is empty
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.email_empty_value)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest37"))
