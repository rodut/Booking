import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class RegisterTest31(unittest.TestCase):
#    driver = webdriver.Chrome()
    # Headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    email = "jacknicholson41@djimail.com"
    confirm_password = "12345678"

    @classmethod
    def setUpClass(cls):
        signin = Register(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_31(self):
        wait = WebDriverWait(self.driver, 10)
        register = Register(self.driver)
        # Click "Register" button
        register.click_register_button()
        # Enter a new valid email account "jacknicholson41@djimail.com"
        register.set_email_address(self.email)
        # Click on "Get started" button
        register.click_get_started_button()
        time.sleep(1)
        # Enter a valid password in "Confirm password" field
        register.set_confirm_password(self.confirm_password)
        # Click "Create account" button
        register.click_create_account_button()
        # Verify if an error message appears ("Please enter your new password")
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.create_pass_error)))
        assert element.is_displayed()
        # Verify if an error message appears ("The passwords you entered didn't match  try again")
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.confirm_pass_error)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="RegisterTest31"))
