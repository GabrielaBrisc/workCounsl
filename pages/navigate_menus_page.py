from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Side_menu_navigation(BasePage):

    #  Scenario: I sign in as consumer to check the left side menus
    EMAIL_FIELD = (By.XPATH, "//div/input[@id='email']")  # //div/div/form/div[1]//*[@id='email']
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")  # //div/div/form/div[2]//*[@id='password']
    LOGIN_BTN = (By.XPATH, "//form/button/span[contains(text(),'Login')]")  # //button[@class="rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center mt-6"]
    OUTSIDE = (By.XPATH, "/html/body/main/section/div/div")
    MESSAGES_MENU = (By.XPATH, "//span[@class='font-medium text-sm text-gray-600'][contains(text(),'Messages')]")
    TEAM_MENU = (By.XPATH, "//span[@class='font-medium text-sm text-gray-600'][contains(text(),'Team')]")
    # CALENDAR_MENU = (By.XPATH, "//span[@class='font-medium text-sm text-gray-600'][contains(text(),'Calendar')]")
    APPOINTMENTS_MENU = (By.XPATH, "//span[@class='font-medium text-sm text-gray-600'][contains(text(),'Appointments')]")
    SEARCH_SERVICES_MENU = (By.XPATH, "//div/a[2]/span[1][contains(text(),'Service search')]")
    WALLET_MENU = (By.XPATH, "//span[@class='font-medium text-sm text-gray-600'][contains(text(),'Wallet')]")
    SETTINGS_MENU = (By.XPATH, "//span[@class='font-medium text-sm text-gray-600'][contains(text(),'Settings')]")
    DONT_SHOW_SEARCH_SYSTEM_MODAL = (By.XPATH, "//div/label/div[@class='Checkbox_container__wQy8Z']")
    CANCEL_BTN_FROM_SEARCH_SYSTEM_MODAL = (By.XPATH, "//div/button/span[contains(text(),'Cancel')]")

    def navigate_to_sign_in(self):
        self.driver.get("https://staging.counsl.dev/login")

    def input_email_address(self, email_address):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email_address)

    def click_outside_field(self):
        self.driver.find_element(*self.OUTSIDE).click()
        sleep(1)

    def input_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        sleep(2)

    def click_outside_field2(self):
        self.driver.find_element(*self.OUTSIDE).click()

    def click_continue_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        sleep(4)


#  Scenario: As a user, I want to navigate through left side menus

    def check_the_dashboard_url(self, url):
        dashboard_url = "https://staging.counsl.dev/dashboard"
        assert url == dashboard_url, f'Error, the message is not in actual message, {dashboard_url}'
        sleep(3)

    def navigate_to_services(self):
        self.driver.find_element(*self.SEARCH_SERVICES_MENU).click()
        sleep(2)

    def click_checkbox_search_system(self):
        self.driver.find_element(*self.DONT_SHOW_SEARCH_SYSTEM_MODAL).click()
        sleep(3)

    def click_cancel_btn_search_system(self):
        self.driver.find_element(*self.CANCEL_BTN_FROM_SEARCH_SYSTEM_MODAL).click()
        sleep(3)

    def check_the_search_services_url(self, url_from_services):
        services_actual_url = "https://staging.counsl.dev/service-search"
        assert services_actual_url == url_from_services, f'Error, the message is not in actual message, {url_from_services}'
        sleep(3)

    def navigate_to_messages(self):
        self.driver.find_element(*self.MESSAGES_MENU).click()

    def check_the_messages_url(self, url_from_messages):
        messages_actual_url = "https://staging.counsl.dev/messages"
        assert messages_actual_url == url_from_messages, f'Error, the message is not in actual message, {url_from_messages}'
        sleep(3)

    def navigate_to_team(self):
        self.driver.find_element(*self.TEAM_MENU).click()

    def check_the_teams_url(self, url_from_team):
        team_actual_url = "https://staging.counsl.dev/team"
        assert team_actual_url == url_from_team, f'Error, the message is not in actual message, {url_from_team}'
        sleep(3)

    def navigate_to_appointments(self):
        self.driver.find_element(*self.APPOINTMENTS_MENU).click()

    def check_the_appointments_url(self, url_from_appointments):
        appointments_actual_url = "https://staging.counsl.dev/appointments"
        assert appointments_actual_url == url_from_appointments, f'Error, the message is not in actual message, {url_from_appointments}'
        sleep(3)

    def navigate_to_wallet(self):
        self.driver.find_element(*self.WALLET_MENU).click()

    def check_the_wallet_url(self, url_from_wallet):
        wallet_actual_url = "https://staging.counsl.dev/wallet"
        assert wallet_actual_url == url_from_wallet, f'Error, the message is not in actual message, {url_from_wallet}'
        sleep(3)

    def navigate_to_settings(self):
        self.driver.find_element(*self.SETTINGS_MENU).click()

    def check_the_settings_url(self, url_from_settings):
        settings_actual_url = "https://staging.counsl.dev/settings"
        assert settings_actual_url == url_from_settings, f'Error, the message is not in actual message, {url_from_settings}'
        sleep(3)
