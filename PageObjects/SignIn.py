from selenium.webdriver.common.keys import Keys
import time

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class SignIn:
    # Locators of all elements
    signin_button = "(//div[@class='sign_in_wrapper'])[2]"  # Using the second from two identical xpaths
    verify_signin = "//h1[text()='Sign in']"
    email_field = "//input[@id='username']"
    next_button = "//span[text()='Next']"
    signup_link = "//a[@data-ga-label='Create account']"
    verify_signup_page = "//h1[text()='Create your account']"
    term_conditions = "//a[@class='bui_color_action nw-terms']"
    verify_term_cond = "//h1[text()='Trip Terms and Conditions']"
    privacy_statement = "//a[@class='bui_color_action nw-privacy']"
    verify_privacy_stat = "//h1[text()='Privacy Statement']"
    confirmation_num_pin = "//a[text()='confirmation number and PIN']"
    verify_conf_num_pin = "//h1[text()='This page is protected for your security']"
    select_lang_de = "//select[@class='lang-select']"
    verify_lang_de = "//h1[text()='Anmelden']"
    hamburger_icon = "//*[@class='bk-icon -iconset-vertical_dots']"
    hamburger_icon_1 = "(//*[@class='bui-dropdown-menu__item'])[1]"
    hamburger_icon_2 = "(//*[@class='bui-dropdown-menu__item'])[2]"
    hamburger_icon_3 = "(//*[@class='bui-dropdown-menu__item'])[3]"
    hamburger_icon_4 = "(//*[@class='bui-dropdown-menu__item'])[4]"
    verify_hamb_icon_1 = "//h1[text()='Create your account']"
    back_arrow = "//*[@data-name='8x']"
    verify_forgot_pass = "//h1[@class='bui_font_display_two bui_font_heading--bold bui-spacer--medium nw-step-header']"
    signin_facebook = "//a[@class='access-panel__social-button access-panel__social-button-facebook bui-button bui-button--secondary nw-social-btn-facebook']"
    verify_signin_fb = "//h2[@id='homelink']"
    signin_google = "//a[@class='access-panel__social-button access-panel__social-button-google bui-button bui-button--secondary nw-social-btn-google']"
    verify_signin_google = "//div[@class='GuHSXd']"
    booking_com_account = "//*[@class='icon-logo']"
    verify_signin_text = "//*[@class='nw-step-description']"
    verify_dont_account = "//div[@class='u-text-center bui-spacer--top']"
    verify_create_acc_agree_text = "//p[text()='By signing in or creating an account, you agree with our ']"
    verify_make_changes_text = "//p[text()='Make changes to a booking with your ']"
    verify_all_rights = "//p[text()='All rights reserved']"
    alert_message_1 = "//div[@id='username-error']"
    create_acc_link = "//a[@class='bui_font_strong bui_color_action']"
    password_field = "//input[@id='password']"
    pass_signin_button = "//button[@class='bui-button bui-button--large bui-button--wide']"
    alert_message_2 = "//div[@id='password-error']"
    verify_success_signin = "//*[@class='bk-icon -sprite-profile_notification bui__profile_notification']"
    your_account = "//*[@class='header_name user_firstname ge-no-yellow-bg']"
    my_dashboard_link = "//div[@class='profile-menu__item profile_menu__item--mydashboard']"
    sign_out_link = "//input[@value='Sign out']"
    x_button = "//button[@class='modal-mask-closeBtn']"
    encrypted_pass = "//input[@type='password']"
    email_empty_value = "//input[@value='']"
    confirm_button = "//span[text()='Confirm']"
    check_inbox = "//h1[text()='Check your inbox']"
    forgot_email = "//input[@id='login_name_recovery']"
    forgot_email_error = "//div[@id='login_name_recovery-error']"
    search_button = "//span[text()='Search']"

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.booking.com"

    def set_forgot_email(self, email):
        self.driver.find_element_by_xpath(self.forgot_email).clear()
        self.driver.find_element_by_xpath(self.forgot_email).send_keys(email)

    def click_confirm_button(self):
        self.driver.find_element_by_xpath(self.confirm_button).click()

    def verify_password(self):
        self.driver.find_element_by_xpath(self.password_field).clear()
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.CONTROL, 'c')
        time.sleep(2)
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.password_field).send_keys(Keys.CONTROL, 'v')

    def click_x_button(self):
        self.driver.find_element_by_xpath(self.x_button).click()

    def click_sign_out_link(self):
        self.driver.find_element_by_xpath(self.sign_out_link).click()

    def click_my_dashboard_link(self):
        self.driver.find_element_by_xpath(self.my_dashboard_link).click()

    def click_your_account(self):
        self.driver.find_element_by_xpath(self.your_account).click()

    def click_password_signin_button(self):
        self.driver.find_element_by_xpath(self.pass_signin_button).click()

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_field).clear()
        self.driver.find_element_by_xpath(self.password_field).send_keys(password)

    def click_create_acc_link(self):
        self.driver.find_element_by_xpath(self.create_acc_link).click()

    def click_next_button(self):
        self.driver.find_element_by_xpath(self.next_button).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.email_field).clear()
        self.driver.find_element_by_xpath(self.email_field).send_keys(email)

    def click_signin_button(self):
        self.driver.find_element_by_xpath(self.signin_button).click()

    def click_signup_link(self):
        self.driver.find_element_by_xpath(self.signup_link).click()

    def click_term_conditions_link(self):
        self.driver.find_element_by_xpath(self.term_conditions).click()

    def switch_next_window_2(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

    def switch_next_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def click_privacy_statement_link(self):
        self.driver.find_element_by_xpath(self.privacy_statement).click()

    def click_confirmation_number_pin(self):
        self.driver.find_element_by_xpath(self.confirmation_num_pin).click()

    def click_hamburger_icon(self):
        self.driver.find_element_by_xpath(self.hamburger_icon).click()

    def click_hamburger_icon_1(self):
        self.driver.find_element_by_xpath(self.hamburger_icon_1).click()

    def click_back_arrow(self):
        self.driver.find_element_by_xpath(self.back_arrow).click()

    def window_back_page(self):
        self.driver.execute_script("window.history.go(-1)")

    def click_hamburger_icon_2(self):
        self.driver.find_element_by_xpath(self.hamburger_icon_2).click()

    def click_hamb_privacy_statement(self):
        self.driver.find_element_by_xpath(self.hamburger_icon_3).click()

    def click_hamb_terms_cond(self):
        self.driver.find_element_by_xpath(self.hamburger_icon_4).click()

    def click_signin_facebook(self):
        self.driver.find_element_by_xpath(self.signin_facebook).click()

    def switch_second_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_signin_google(self):
        self.driver.find_element_by_xpath(self.signin_google).click()
