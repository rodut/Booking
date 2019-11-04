import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from PageObjects.SignIn import SignIn
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/Booking")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class SignInTest05(unittest.TestCase):
    # Headless Firefox
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    @classmethod
    def setUpClass(cls):
        signin = SignIn(cls.driver)
        cls.driver.maximize_window()
        cls.driver.get(signin.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_signin_05(self):
        wait = WebDriverWait(self.driver, 10)
        signin = SignIn(self.driver)
        # Click "Sign in" button
        signin.click_signin_button()
        time.sleep(1)
        # Click on "Terms & Conditions" link
        signin.click_term_conditions_link()
        time.sleep(2)
        # Switch to next window in browser
        signin.switch_next_window_2()
        # Verify if "Terms & Conditions" link was opened
        element = wait.until(EC.presence_of_element_located((By.XPATH, SignIn.verify_term_cond)))
#        element = self.driver.find_element_by_xpath(SignIn.verify_term_cond)
        assert element.is_displayed()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\Booking\\Reports",
        report_name="SignInTest05"))
