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


class SignInTest35(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "jacknicholson@djimail.com"
    password = "  12345678"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_35(self):
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
        # Enter two blank spaces before entering the valid password ("  12345678")
        signin.set_password(self.password)
        # Click "Sign in" button
        signin.click_password_signin_button()
        # Verify if user was logged in successfully
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.verify_success_signin)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest35"))
