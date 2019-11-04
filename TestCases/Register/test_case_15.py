import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from PageObjects.Register import Register
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class RegisterTest15(unittest.TestCase):
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

    def test_register_15(self):
        register = Register(self.driver)
        # Click "Register" button
        register.click_register_button()
        # Click on hamburger icon
        register.click_hamburger_icon()
        # Click on "Terms & conditions" link
        register.click_hamburger_terms_conds()
        time.sleep(1)
        # Switch to new opened window
        register.switch_next_window()
        # Verify if "Terms & conditions" link was opened in a new window
        assert "Booking.com: Terms and Conditions." in self.driver.title


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="RegisterTest15"))
