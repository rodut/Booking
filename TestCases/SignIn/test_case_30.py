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


class SignInTest30(unittest.TestCase):
    driver = webdriver.Chrome()
    email = "abracadabra@djimail.com"

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_30(self):
        wait = WebDriverWait(self.driver, 10)
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Enter an inactive (deleted) email (abracadabra@djimail.com)
        signin.set_email(self.email)
        # Click on "Next" button
        signin.click_next_button()
        # Verify if an error message appears (Looks like there isn't an account associated with this email address...)
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.alert_message_1)))
        assert element.is_displayed()
        # Click on "create an account" link
        signin.click_create_acc_link()
        # Verify if the form changed to "Create your account"
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.verify_signup_page)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest30"))
