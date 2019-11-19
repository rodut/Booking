import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"


class RegisterTest17(unittest.TestCase):
    # Headless Firefox browser
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    @classmethod
    def setUpClass(cls):
        signin = Register(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_17(self):
        register = Register(self.driver)
        # Click "Register" button
        register.click_register_button()
        # Click on "Sign in with Google"
        register.click_google_signin()
        time.sleep(1)
        # Switch to the new opened tab
        register.switch_second_tab()
        # Verify if a new tab was opened asking you to login to your Google account
        assert "Conectați-vă – Conturi Google" in self.driver.title


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="RegisterTest17"))
