from time import sleep

#from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#from selenium.webdriver.common.action_chains import ActionChains

class OnboardingConsumer(BasePage):
    FIND_PROFESSIONALS_BTN = (By.XPATH,"//span[contains(text(),'Find Professionals')]") # de incercat si cu acesta [fdprocessedid="gy0679"]
    OFFER_SERVICES_BTN = (By.XPATH,"//div/button[2]/span")
    EMAIL_FIELD = (By.XPATH, "//form/child::div/input")
    PASSWORD_FIELD = (By.XPATH, "//form/child::div[2]/input")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//form/child::div[3]/input") #//form/child::div[3]/input[@id='confirmPassword']
    TERMS_PRIVACY_CHECKBOX = (By.XPATH, "//*[@id='checkbox-input']")  #//div/span[@class="Checkbox_checkmark__M5c5x"]
    SIGN_UP_BTN = (By.XPATH, "//button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center mt-6']")

    #scenario 3:   Scenario: Input company house no. on the Create a company screen
    COMPANY_HOUSE_NO =  (By.XPATH, "//div/input[@id='house-number']")
    CONTINUE_CREATE_ACCOUNT1_BTN = (By.XPATH,"//div//button/span[@class='leading-[1.25rem]']")


    #  Scenario: I want to choose between the 2 options from create account screen
    def navigate_to_create_account(self):
        self.driver.get("https://staging.counsl.dev/create-account")

    def click_on_find_professionals(self):
        self.driver.find_element(*self.FIND_PROFESSIONALS_BTN).click()

    #onboarding - second screen of create account
    #Scenario: Enter the credentials to create the account

    def check_the_current_url(self, url):
        actual_url = "https://staging.counsl.dev/consumer/signup"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def fill_in_email_field(self, email_address):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email_address)

    def fill_in_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        sleep(2)
    def fill_in_confirm_password_field(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password)
        sleep(1)

    def agree_terms_policy_checkbox(self):
        self.driver.find_element(*self.TERMS_PRIVACY_CHECKBOX).click()
        sleep(2)

    def click_continue_from_create_account(self):
        self.driver.find_element(*self.SIGN_UP_BTN).click()
        sleep(1)

    #Scenario: Input company house no. on the Create a company screen
    # def check_the_create_account_url(self, url):
    #     actual_url = "https://staging.counsl.dev/consumer/create-company/address"
    #     assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def clear_company_house_no(self):
        self.driver.find_element(*self.COMPANY_HOUSE_NO).click()
        sleep(2)

    def input_company_house_no(self, company_house_no):
        self.driver.find_element(*self.COMPANY_HOUSE_NO).send_keys(company_house_no)
        sleep(2)

    def click_continue_from_create_company1(self):
        self.driver.find_element(*self.CONTINUE_CREATE_ACCOUNT1_BTN).click()
        sleep(3)

        #  Scenario: Add the company logo
    UPLOAD_BTN = (By.XPATH, "//div/button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-white border-gray-300 text-gray-700 border h-[30px] text-sm h-[50px] flex justify-center items-center']")
    CONTINUE_ADD_LOGO = (By.XPATH,
                             "//div//button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] opacity-50 w-full flex justify-center items-center mt-10']")

    #ar trebui sa gasesc o metoda care sa adauge direct acel company house no in url
    # def check_the_add_logo_url(self, url):
    #     actual_url = "https://staging.counsl.dev/consumer/create-company/details?houseNumber=14586847"
    #     assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    # def click_upload_btn(self):
    #     self.driver.find_element(*self.UPLOAD_BTN).click()

    def upload_logo(self):
        self.driver.find_element(*self.UPLOAD_BTN).send_keys("C:/Users/Gabriela/PycharmProjects/workCounsl/pictures/thank you1.jpg")
        sleep(3)

    def click_continue_from_add_logo(self):
        self.driver.find_element(*self.CONTINUE_ADD_LOGO).click()
        sleep(2)

# third screen from create company
#  Scenario: Fill in all the fields from Create a company third screen
    #  Make a personal profile screen
# link = https://staging.counsl.dev/consumer/create-company/personal-profile
    FIRST_NAME = (By.XPATH, "//div/input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//div/input[@id='last-name']")
    JOB_TITLE = (By.XPATH, "//div/input[@id='position']")
    CONTINUE_PERSONAL_PROFILE = (By.XPATH, "//form/button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center mt-6']")

    def check_the_make_profile_url(self, url):
        actual_url = "https://staging.counsl.dev/consumer/create-company/personal-profile"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def input_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def input_job_title(self, job_title):
        self.driver.find_element(*self.JOB_TITLE).send_keys(job_title)

    def click_continue_from_make_personal_profile(self):
        self.driver.find_element(*self.CONTINUE_PERSONAL_PROFILE).click()


#  Scenario: Fill in all the fields from Tell Us About Your Business screen
    COMPANY_SIZE = (By.XPATH, "//div/input[@id='company-size']")
    ABOUT_YOUR_COMPANY = (By.XPATH, "//div/textarea[@id='company-description']")
    PRESSING_PROBLEM_DESCRIPTION = (By.XPATH, "//div/textarea[@id='problem']")
    CONTINUE_ABOUT_BUSINESS = (By.XPATH, "//button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center mt-6']")
    #//button/span[@class="leading-[1.25rem]"]

    def check_the_about_business_url(self, url):
        actual_url = "https://staging.counsl.dev/consumer/create-company/business-details"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def input_company_size(self, company_size_no):
        self.driver.find_element(*self.COMPANY_SIZE).send_keys(company_size_no)

    def input_about_company(self, about_company):
        self.driver.find_element(*self.ABOUT_YOUR_COMPANY).send_keys(about_company)

    def input_pressing_problem(self, pressing_problem):
        self.driver.find_element(*self.ABOUT_YOUR_COMPANY).send_keys(pressing_problem)

    def click_continue_about_business(self):
        self.driver.find_element(*self.CONTINUE_PERSONAL_PROFILE).click()

#  Scenario: Choose the basic plan
    SUBSCRIBE_BASIC_PLAN = (By.XPATH, "//div[1]/div[1]/div[2]/button/div/span[@class='Text Text-color--default Text-fontWeight--500 Text--truncate']")

    def check_the_plans_url(self, url):
        actual_url = "https://staging.counsl.dev/consumer/become-member"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def click_subscribe_basic_plan(self):
        self.driver.find_element(*self.SUBSCRIBE_BASIC_PLAN).click()

 #  Scenario: Fill in the credit cards details from stripe
    EMAIL_STRIPE_FIELD = (By.XPATH, "//div[@id='email-fieldset']")
    CARD_NO = (By.XPATH, "//div/span/input[@id='cardNumber']")
    MONTH_YEAR = (By.XPATH, "//span/input[@id='cardExpiry']")
    CVC_CARD = (By.XPATH, "//span/input[@id='cardCvc']")
    CARDHOLDER_NAME = (By.XPATH, "//span/input[@id='billingName']")
    PAY_BTN = (By.XPATH, "//span[contains(text(),'Pay and subscribe')]")

    def input_email_stripe_field(self, email_stripe):
        self.driver.find_element(*self.EMAIL_STRIPE_FIELD).send_keys(email_stripe)

    def input_card_no_field(self, credit_card_no):
        self.driver.find_element(*self.CARD_NO).send_keys(credit_card_no)

    def input_month_year_field(self, month_year_credit_card):
        self.driver.find_element(*self.CARD_NO).send_keys(month_year_credit_card)

    def input_cvc_card_info(self, cvc_card):
        self.driver.find_element(*self.CVC_CARD).send_keys(cvc_card)

    def input_name_from_card(self, name_from_card):
        self.driver.find_element(*self.CVC_CARD).send_keys(name_from_card)

    def click_pay_btn_stripe(self):
        self.driver.find_element(*self.PAY_BTN).click()

  #  Scenario: Click on Continue button from Payment successful screen
    CONTINUE_PAYMENT_SUCCESSFUL = (By.XPATH, "//span[contains(text(),'Continue')]")

    def check_payment_successful_url(self, url):
        actual_url = "https://staging.counsl.dev/consumer/become-member/success"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def click_continue_from_payment_successful(self):
        self.driver.find_element(*self.CONTINUE_PAYMENT_SUCCESSFUL).click()

#  Scenario: Fill in the directors email
    ADD_DIRECTORS_EMAIL = (By.XPATH, "//span[contains(text(),'Add Email')]")
    CONTINUE_SEND_VERIFICATION = (By.XPATH, "//span[contains(text(),'Continue and Send Verification Emails')]")
    DIRECTOR_EMAIL_FIELD = (By.XPATH, "//form/div/input[@id='email']")
    ADD_EMAIL_BTN_FROM_MODAL = (By.XPATH, "//div/div/button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center w-full max-w-[104px]']")
    CANCEL_EMAIL_BTN = (By.XPATH, "//div/div/button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-white border-gray-300 text-gray-700 border h-[30px] text-sm h-[50px] w-full flex justify-center items-center w-full max-w-[104px] mr-3']")


    def check_verify_business_url(self, url):
        actual_url = "https://staging.counsl.dev/consumer/verify-business"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def click_add_director_email(self):
        self.driver.find_element(*self.ADD_DIRECTORS_EMAIL).click()

    def input_directors_email(self, directors_email):
        self.driver.find_element(*self.DIRECTOR_EMAIL_FIELD).send_keys(directors_email)

    def click_add_btn_to_close_modal(self):
        self.driver.find_element(*self.ADD_EMAIL_BTN_FROM_MODAL).click()

    def click_continue_send_verification_emails(self):
        self.driver.find_element(*self.CONTINUE_SEND_VERIFICATION).click()


 #  Scenario: Add a team member
    ADD_MEMBER_BTN = (By.XPATH, "//div/button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-indigo-50 text-indigo-700 text-sm h-[38px] w-full flex justify-center items-center hover:opacity-80']")
    FIRST_NAME_TEAM_MEMBER = (By.XPATH, "//div/input[@id='firstName']")
    LAST_NAME_TEAM_MEMBER = (By.XPATH, "//div/input[@id='lastName']")
    EMAIL_TEAM_MEMBER = (By.XPATH, "//div/input[@id='email']")
    JOB_TITLE_TEAM_MEMBER = (By.XPATH, "//div/input[@id='position']")
    ADD_TEAM_MEMBER_FROM_MODAL = (By.XPATH, "//div/input[@id='position']")
    CONTINUE_ADD_MEMBER = (By.XPATH, "//div/button[@class='rounded-md shadow-sm relative py-2 px-3 whitespace-nowrap bg-brand-1 text-white text-sm h-[50px] w-full flex justify-center items-center mt-10']")

    def check_create_profiles_url(self, url):
        actual_url = "https://staging.counsl.dev/consumer/team-and-services/create-profiles"
        assert url == actual_url, f'Error, the message is not in actual message, {actual_url}'

    def click_add_team_member(self):
        self.driver.find_element(*self.ADD_MEMBER_BTN).click()

    def input_member_first_name(self, members_first_name):
        self.driver.find_element(*self.FIRST_NAME_TEAM_MEMBER).send_keys(members_first_name)

    def input_member_last_name(self,members_last_name):
        self.driver.find_element(*self.LAST_NAME_TEAM_MEMBER).send_keys(members_last_name)

    def input_member_email(self, members_email):
        self.driver.find_element(*self.EMAIL_TEAM_MEMBER).send_keys(members_email)

    def input_member_job_title(self, members_job_title):
        self.driver.find_element(*self.JOB_TITLE_TEAM_MEMBER).send_keys(members_job_title)

    def click_add_btn_from_modal(self):
        self.driver.find_element(*self.ADD_TEAM_MEMBER_FROM_MODAL).click()

    def click_continue_from_add_member_screen(self):
        self.driver.find_element(*self.CONTINUE_ADD_MEMBER).click()



