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


class RegisterTest13(unittest.TestCase):
    # driver = webdriver.Chrome()
    # Headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def setUpClass(cls):
        signin = Register(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_13(self):
        wait = WebDriverWait(self.driver, 10)
        register = Register(self.driver)
        # Click "Register" button
        register.click_register_button()
        # Click on hamburger icon
        register.click_hamburger_icon()
        # Click on "Sign in" link
        register.click_hamburger_signin()
        # Verify if the form changed to "Sign in"
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.verify_signin)))
        assert element.is_displayed()
        # Click back arrow (next to "Booking.com Account")
        register.click_back_arrow()
        # Verify if the form changed to "Create your account"
        element = wait.until(EC.presence_of_element_located((By.XPATH, Register.verify_register)))
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="RegisterTest13"))
