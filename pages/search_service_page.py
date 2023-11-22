from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class SearchService(BasePage):

    #  Scenario: I sign in as consumer
    EMAIL_FIELD = (By.XPATH, "//div/input[@id='email']")  # //div/div/form/div[1]//*[@id='email']
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")  # //div/div/form/div[2]//*[@id='password']
    LOGIN_BTN = (By.XPATH, "//form/button/span[contains(text(),'Login')]")  # //button[@class="rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center mt-6"]
    OUTSIDE = (By.XPATH, "/html/body/main/section/div/div")

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

    #  Scenario: I am a consumer on the search screen and I search for a service
    SEARCH_FIELD = (By.XPATH, "//form/div/input[@placeholder='Enter your search detail']")
    SUBMIT_SEARCH = (By.XPATH, "//div/button[@type='submit']")
    SERVICES_MENU = (By.XPATH, "//div/a[2]/span[1][contains(text(),'Service search')]")
    DONT_SHOW_SEARCH_SYSTEM_MODAL = (By.XPATH, "//div/label/div[@class='Checkbox_container__wQy8Z']")
    CANCEL_BTN_FROM_SEARCH_SYSTEM_MODAL = (By.XPATH, "//div/button/span[contains(text(),'Cancel')]")

    def navigate_to_service_search(self):
        self.driver.find_element(*self.SERVICES_MENU).click()
        sleep(5)

#pentru modala care apare, ar trebui sa verific daca a aparut
    # si dupa sa fac partea cu check box ?
    def click_checkbox_search_system(self):
        self.driver.find_element(*self.DONT_SHOW_SEARCH_SYSTEM_MODAL).click()
        sleep(3)

    def click_cancel_btn_search_system(self):
        self.driver.find_element(*self.CANCEL_BTN_FROM_SEARCH_SYSTEM_MODAL).click()

    def input_search_details(self, search_details):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(search_details)
        sleep(3)

    def click_submit_search_btn(self):
        self.driver.find_element(*self.SUBMIT_SEARCH).click()
        sleep(3)

