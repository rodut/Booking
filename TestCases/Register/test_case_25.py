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


class RegisterTest25(unittest.TestCase):
    # Headless Firefox
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

    def test_register_25(self):
        register = Register(self.driver)
        # Click "Register" button
        register.click_register_button()
        # Click on "Booking.com for Business?" link
        register.click_booking_business_link()
        time.sleep(1)
        # Switch to new opened window
        register.switch_next_window()
        # Verify if "Booking.com for Business" page was opened in a new window
        assert "Booking.com for Business – free business travel management from Booking.com" in self.driver.title


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="RegisterTest25"))
