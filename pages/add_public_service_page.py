#from selenium.common import NoSuchElementException
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#from selenium.webdriver.common.action_chains import ActionChains

class AddPublicService(BasePage):


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

    def click_outside_field2(self):
        self.driver.find_element(*self.OUTSIDE).click()

    def click_continue_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        sleep(1)


#  Scenario: I go to service page and add a draft service
    SERVICES_MENU = (By.XPATH, "//div/a/span[1][contains(text(),'Services')]")
    ADD_SERVICE_BUTTON = (By.XPATH, "//div/button/span[contains(text(),'Add Services')]")
    SERVICE_NAME_MODAL_FIELD = (By.XPATH, "//div/input[@id='name']")
    SERVICE_TYPE_MODAL_FIELD = (By.XPATH, "//div/input[@id='type']")
    TAGS_MODAL_FIELD = (By.XPATH, "//div/input[@id='tags']")
    ABOUT_SERVICE_MODAL_FIELD = (By.XPATH, "//div/textarea[@id='about']")
    IMAGE_COVER_FIELD = (By.XPATH, "//div[@role='presentation']")
    UPLOAD_IMAGE_COVER_BTN = (By.XPATH, "//div/p/span[contains(text(),'Upload a file')]")
    DRAFT_RADIO_BTN = (By.XPATH, "//div/input[@id='Draft']")
    PUBLIC_RADIO_BTN = (By.XPATH, "//div/input[@id='Public']")
    SAVE_SERVICE_MODAL_BTN = (By.XPATH, "//div/button[2]/span[contains(text(),'Save')]")
    CANCEL_SERVICE_MODAL_BTN = (By.XPATH, "//div/button[1]/span[contains(text(),'Cancel')]")
    LIST_OF_PUBLIC_SERVICES_ADDED = (By.XPATH, "//section/div[1]/div[2]/div")


    def check_the_dashboard_url(self, url):
        dashboard_url = "https://staging.counsl.dev/dashboard"
        assert url == dashboard_url, f'Error, the message is not in actual message, {dashboard_url}'
        sleep(1)

    def click_on_service_left_menu(self):
        self.driver.find_element(*self.SERVICES_MENU).click()
        sleep(1)

    def click_add_service_btn(self):
        self.driver.find_element(*self.ADD_SERVICE_BUTTON).click()

    def input_service_name(self, service_name):
        self.driver.find_element(*self.SERVICE_NAME_MODAL_FIELD).send_keys(service_name)
        sleep(1)

    def input_service_type(self, service_type):
        self.driver.find_element(*self.SERVICE_TYPE_MODAL_FIELD).send_keys(service_type)

    def input_tags(self, tags):
        self.driver.find_element(*self.TAGS_MODAL_FIELD).send_keys(tags)
        sleep(2)

    def hit_enter_tags(self):
        self.driver.find_element(*self.TAGS_MODAL_FIELD).send_keys(Keys.ENTER)
        sleep(2)

    def input_about_service_details(self, about_service):
        self.driver.find_element(*self.ABOUT_SERVICE_MODAL_FIELD).send_keys(about_service)
        sleep(2)

    def upload_image_cover(self):
        self.driver.find_element(*self.IMAGE_COVER_FIELD).send_keys("C:/Users/Gabriela/PycharmProjects/workCounsl/pictures/thank you1.jpg")
        sleep(5)

##the public radio btn is selected by default

    def click_save_service_btn(self):
        self.driver.find_element(*self.SAVE_SERVICE_MODAL_BTN).click()
        sleep(3)

    #verify if the new service was successfully added:
        #steps:
    #verific cate am initial, inainte sa adaug un serviciu nou: cate servicii am in lista?
    #adaug serviciul
    #verific daca s a mai adaugat unul

#verific cate elemente am in lista:
    def verify_the_no_of_services(self):
        list_of_public_services = self.driver.find_elements(*self.LIST_OF_PUBLIC_SERVICES_ADDED)
        # print("Numarul de servicii publice adaugate este:",len(list_of_public_services))
        return len(list_of_public_services)