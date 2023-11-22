from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class Sign_in(BasePage):
    EMAIL_FIELD = (By.XPATH, "//div/input[@id='email']")  #//div/div/form/div[1]//*[@id='email']
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password']") #//div/div/form/div[2]//*[@id='password']
    LOGIN_BTN = (By.XPATH, "//form/button/span[contains(text(),'Login')]")    # //button[@class="rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center mt-6"]
    OUTSIDE = (By.XPATH, "/html/body/main/section/div/div")

    def navigate_to_sign_in(self):
        self.driver.get("https://staging.counsl.dev/login")

    def input_email_address(self,email_address):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email_address)

    def click_outside_field(self):
        self.driver.find_element(*self.OUTSIDE).click()
        sleep(1)

    def input_password(self,password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        sleep(2)

    def click_outside_field2(self):
        self.driver.find_element(*self.OUTSIDE).click()

    def click_continue_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        sleep(2)

    def check_the_current_url(self, url):
        dashboard_url = "https://staging.counsl.dev/dashboard"
        assert url == dashboard_url, f'Error, the message is not in actual message, {dashboard_url}'
        sleep(3)