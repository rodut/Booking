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


class RegisterTest04(unittest.TestCase):
    # driver = webdriver.Chrome()
    # Headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    email = "jacknicholson@djimailcom"

    @classmethod
    def setUpClass(cls):
        signin = Register(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_04(self):
        wait = WebDriverWait(self.driver, 10)
        register = Register(self.driver)
        # Click "Register" button
        register.click_register_button()
        # Enter an email with incorrect format (jacknicholson@djimailcom)
        register.set_email_address(self.email)
        # Click Click on "Get started" button
        register.click_get_started_button()
        # Verify if an error message appears (Make sure the email address you entered is correct.)
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.error_email_message)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="RegisterTest04"))
