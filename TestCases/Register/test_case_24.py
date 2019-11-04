import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest24(unittest.TestCase):
    # driver = webdriver.Chrome()
    # Headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    email = "jacknicholson41@djimail.com"

    @classmethod
    def setUpClass(cls):
        signin = Register(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_24(self):
        wait = WebDriverWait(self.driver, 10)
        register = Register(self.driver)
        # Click "Register" button
        register.click_register_button()
        # Enter a valid email account (jacknicholson41@djimail.com)
        register.set_email_address(self.email)
        # Click on "Get started" button
        register.click_get_started_button()
        # Check if "Create password" field is present
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.create_pass_field)))
        assert element.is_displayed()
        # Check if "Confirm password" field is present
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.confirm_pass_field)))
        assert element.is_displayed()
        # Check if "Create account" button is present
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.create_acc_button)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="RegisterTest24"))
