from selenium.webdriver.support.ui import Select

__author__ = "Chirosca Tudor"
__email__ = "tudorache@gmail.com"


class Register:
    # Locators of all elements
    register_button = "(//div[@class='sign_in_wrapper'])[1]"
    verify_register = "//h1[text()='Create your account']"
    email_field = "//input[@id='login_name_register']"
    get_started_button = "//span[text()='Get started']"
    error_email_message = "//div[@id='login_name_register-error']"
    signin_here_link = "//a[@class='bui_font_strong bui_color_action']"
    verify_signin = "//h1[text()='Sign in']"
    terms_conds_link = "//a[@class='bui_color_action nw-terms']"
    privacy_state_link = "//a[@class='bui_color_action nw-privacy']"
    conf_num_pin_link = "//a[text()='confirmation number and PIN']"
    select_lang_de = "//select[@class='lang-select']"
    verify_lang_de = "//h1[text()='Erstellen Sie Ihr Konto']"
    hamburger_icon = "//*[@class='bk-icon -iconset-vertical_dots']"
    hamburger_signin = "//span[text()='Sign in']"
    hamburger_priv_stat = "//span[text()='Privacy statement']"
    hamburger_terms_conds = "//span[text()='Terms & conditions']"
    back_arrow = "//*[@data-name='8x']"
    facebook_signin = "//div[text()='Sign in with Facebook']"
    google_signin = "//div[text()='Sign in with Google']"
    booking_acc_logo = "//span[@class='access-panel__header-logo']"
    create_acc_desc = "//p[@class='nw-step-description']"
    already_have_acc = "//div[@class='u-text-center bui-spacer--top']"
    sign_create_acc = "//p[@class='account_footer_terms']"
    make_changes_booking = "//p[text()='Make changes to a booking with your ']"
    all_rights_reserved = "//p[text()='All rights reserved']"
    create_pass_field = "//input[@id='password']"
    confirm_pass_field = "//input[@id='confirmed_password']"
    create_acc_button = "//button[@class='bui-button bui-button--large bui-button--wide']"
    booking_business_link = "//a[text()='Booking.com for Business?']"
    booking_business_text = "//p[text()='Interested in ']"
    rent_your_place = "//p[text()='Rent out your place on Booking.com']"
    list_property_link = "//a[text()='List Your Property']"
    verify_email_text = "//strong[text()='jacknicholson41@djimail.com']"
    confirm_pass_error = "//div[@id='confirmed_password-error']"
    create_pass_error = "//div[@id='password-error']"
    confirm_register = "//*[@class='bk-icon -sprite-profile_notification bui__profile_notification']"

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.booking.com"

    def click_create_account_button(self):
        self.driver.find_element_by_xpath(self.create_acc_button).click()

    def click_list_property_link(self):
        self.driver.find_element_by_xpath(self.list_property_link).click()

    def click_booking_business_link(self):
        self.driver.find_element_by_xpath(self.booking_business_link).click()

    def click_google_signin(self):
        self.driver.find_element_by_xpath(self.google_signin).click()

    def click_facebook_signin(self):
        self.driver.find_element_by_xpath(self.facebook_signin).click()

    def switch_second_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_hamburger_terms_conds(self):
        self.driver.find_element_by_xpath(self.hamburger_terms_conds).click()

    def click_hamburger_priv_stat(self):
        self.driver.find_element_by_xpath(self.hamburger_priv_stat).click()

    def click_back_arrow(self):
        self.driver.find_element_by_xpath(self.back_arrow).click()

    def click_hamburger_signin(self):
        self.driver.find_element_by_xpath(self.hamburger_signin).click()

    def click_hamburger_icon(self):
        self.driver.find_element_by_xpath(self.hamburger_icon).click()

    def set_select_lang_de(self):
        element = self.driver.find_element_by_xpath(Register.select_lang_de)
        dropdown = Select(element)
        dropdown.select_by_value("de")

    def click_conf_num_pin_link(self):
        self.driver.find_element_by_xpath(self.conf_num_pin_link).click()

    def click_privacy_state_link(self):
        self.driver.find_element_by_xpath(self.privacy_state_link).click()

    def switch_next_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def click_terms_conds_link(self):
        self.driver.find_element_by_xpath(self.terms_conds_link).click()

    def click_signin_here_link(self):
        self.driver.find_element_by_xpath(self.signin_here_link).click()

    def click_register_button(self):
        self.driver.find_element_by_xpath(self.register_button).click()

    def set_password_address(self, password):
        self.driver.find_element_by_xpath(self.create_pass_field).clear()
        self.driver.find_element_by_xpath(self.create_pass_field).send_keys(password)

    def set_confirm_password(self, confirm_password):
        self.driver.find_element_by_xpath(self.confirm_pass_field).clear()
        self.driver.find_element_by_xpath(self.confirm_pass_field).send_keys(confirm_password)

    def set_email_address(self, email):
        self.driver.find_element_by_xpath(self.email_field).clear()
        self.driver.find_element_by_xpath(self.email_field).send_keys(email)

    def click_get_started_button(self):
        self.driver.find_element_by_xpath(self.get_started_button).click()

