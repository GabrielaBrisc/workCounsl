from behave import *

# Scenario: I want to choose between the 2 options from create account screen
@Given("accountprovider: I am a user on the create account first screen")
def step_impl(context):
    context.onboarding_provider_page.navigate_to_create_account()

@Then("accountprovider: I click on Find Professionals button")
def step_impl(context):
    context.onboarding_provider_page.click_on_find_professionals()

# second screen from create account
# Scenario: Enter the credentials to create the account
@Given('accountprovider: I am a user on the create account second screen "{url1}"')
def step_impl(context, url1):
    context.onboarding_provider_page.check_the_current_url(url1)

@When('accountprovider: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.onboarding_provider_page.fill_in_email_field(email_address)

@When('accountprovider: I fill in the password field "{password}"')
def step_impl(context, password):
    context.onboarding_provider_page.fill_in_password_field(password)

@When('accountprovider: I fill in the confirm password field "{confirm_password}"')
def step_impl(context, confirm_password):
    context.onboarding_provider_page.fill_in_confirm_password_field(confirm_password)

@When("accountprovider: I click on the checkbox to agree with terms and policy")
def step_impl(context):
    context.onboarding_provider_page.agree_terms_policy_checkbox()

@Then("accountprovider: I click on the Sign Up button")
def step_impl(context):
    context.onboarding_provider_page.click_continue_from_create_account()

#create company first screen
#Scenario: Input company house no. on the Create a company screen
# @Given('accountprovider: I am a user on the Create a company screen "{url2}"')
# def step_impl(context, url2):
#     context.onboarding_provider_page.check_the_create_account_url(url2)

# @When("accountprovider: I clear the input field")
# def step_impl(context):
#     context.onboarding_provider_page.clear_company_house_no()

# @Then('accountprovider: I input the companies house no. "{company_house_no}"')
# def step_impl(context,company_house_no):
#     context.onboarding_provider_page.input_company_house_no(company_house_no)
#
# @Then("accountprovider: I click on Continue button")
# def step_impl(context):
#     context.onboarding_provider_page.click_continue_from_create_company1()
#
#
# #create company second screen
# #  Scenario: Add the company logo
#
# @Given('accountprovider: I am a user on the Create a company second screen "{url3}')
# def step_impl(context, url_add_logo_screen):
#     context.onboarding_provider_page.check_the_add_logo_url(url_add_logo_screen)
#
# @When("accountprovider: I click on Upload button")
# def step_impl(context):
#     context.onboarding_provider_page.click_upload_btn()
#
# @When("accountprovider: I upload the logo")
# def step_impl(context):
#     context.onboarding_provider_page.upload_logo()
#
# @Then("accountprovider: I click on Continue button from add logo screen")
# def step_impl(context):
#     context.onboarding_provider_page.click_continue_from_add_logo()
#
#
# # third screen from create company
# #  Scenario: Fill in all the fields from Create a company third screen
#     #  Make a personal profile screen
# # link = https://staging.counsl.dev/consumer/create-company/personal-profile
#
# @Given('accountprovider: I am a user on the Make a personal profile screen "{url3}')
# def step_impl(context, url3):
#     context.onboarding_provider_page.check_the_make_profile_url(url3)
#
# @When('accountprovider: I input the first name "{first_name}"')
# def step_impl(context, first_name):
#     context.onboarding_provider_page.input_first_name(first_name)
#
# @When('accountprovider: I input the last name "{last_name}"')
# def step_impl(context, last_name):
#     context.onboarding_provider_page.input_first_name(last_name)
#
# @When('accountprovider: I input the job title "{job_title}"')
# def step_impl(context, job_title):
#     context.onboarding_provider_page.input_first_name(job_title)
#
# @Then("accountprovider: I click on Continue button from Make a personal profile screen")
# def step_impl(context):
#     context.onboarding_provider_page.click_continue_from_make_personal_profile()
#
#
# #  Scenario: Fill in all the fields from Tell Us About Your Business screen
# @Given('accountprovider: I am a user on the Tell Us About Your Business screen "{url_about_business}"')
# def step_impl(context, url_about_business):
#     context.onboarding_provider_page.check_the_about_business_url(url_about_business)
#
# @When('accountprovider: I fill in the company size field "{company_size}"')
# def step_impl(context, company_size):
#     context.onboarding_provider_page.input_company_size(company_size)
#
# @When('accountprovider: I fill in the Tell Us About Your Company field "{about_company}')
# def step_impl(context, about_company):
#     context.onboarding_provider_page.input_about_company(about_company)
#
# @When('accountprovider: I fill in the Tell Us About Your Company field "{about_company}')
# def step_impl(context, about_company):
#     context.onboarding_provider_page.input_about_company(about_company)
#
# @When('accountprovider: I fill in the What is the most pressing problem you are having today? field "{pressing_problem}')
# def step_impl(context, pressing_problem):
#     context.onboarding_provider_page.input_pressing_problem(pressing_problem)
#
# @Then("accountprovider: I click on continue button from Tell Us About Your Business screen")
# def step_impl(context):
#     context.onboarding_provider_page.click_continue_about_business()
#
#
# #  Scenario: Choose the basic plan
# @Given('accountprovider: I am a user on the Plans screen "{url_plans}"')
# def step_impl(context, url_plans):
#     context.onboarding_provider_page.check_the_plans_url(url_plans)
#
# @Then("accountprovider: I click on the desired plan")
# def step_impl(context):
#     context.onboarding_provider_page.click_subscribe_basic_plan()
#
#
# #  Scenario: Fill in the credit cards details from stripe
# @When('accountprovider: I input the email field "{email_stripe}"')
# def step_impl(context, email_stripe):
#     context.onboarding_provider_page.input_email_stripe_field(email_stripe)
#
# @When('accountprovider: I input the card number field "{credit_card_no}"')
# def step_impl(context, credit_card_no):
#     context.onboarding_provider_page.input_card_no_field(credit_card_no)
#
# @When('accountprovider: I input the month and year field "{month_year_date}"')
# def step_impl(context, month_year_date):
#     context.onboarding_provider_page.input_month_year_field(month_year_date)
#
# @When('accountprovider: I input the CVC field "{cvc_card_info}"')
# def step_impl(context, cvc_card_info):
#     context.onboarding_provider_page.input_cvc_card_info(cvc_card_info)
#
# @When('accountprovider: I input the name on card "{name_from_card}"')
# def step_impl(context, name_from_card):
#     context.onboarding_provider_page.input_name_from_card(name_from_card)
#
# @Then("accountprovider: I click on the Payment button")
# def step_impl(context):
#     context.onboarding_provider_page.click_pay_btn_stripe()
#
#
#   #  Scenario: Click on Continue button from Payment successful screen
# @Given('accountprovider: I am a user on the Payment successful screen "{url_payment_successful}"')
# def step_impl(context, url_payment_successful):
#     context.onboarding_provider_page.check_payment_successful_url(url_payment_successful)
#
# @Then("accountprovider: I click on Continue button")
# def step_impl(context):
#     context.onboarding_provider_page.click_continue_from_payment_successful()
#
#
# #  Scenario: Fill in the directors email
# @Given('accountprovider: I am a user on the Verify your business screen "{url_verify_business}"')
# def step_impl(context, url_verify_business):
#     context.onboarding_provider_page.check_verify_business_url(url_verify_business)
#
# @When("accountprovider: I click on add email button")
# def step_impl(context):
#     context.onboarding_provider_page.click_add_director_email()
#
# @When('accountprovider: I fill in the email field "{directors_email}"')
# def step_impl(context,directors_email):
#     context.onboarding_provider_page.input_directors_email(directors_email)
#
# @Then("accountprovider: Click on add button and the modal is closed")
# def step_impl(context):
#     context.onboarding_provider_page.click_add_btn_to_close_modal()
#
# @Then("accountprovider: I click on the Continue and Send Verification Emails btn")
# def step_impl(context):
#     context.onboarding_provider_page.click_continue_send_verification_emails()
#
#
# #   Scenario: Add a team member
# @Given('accountprovider: I am a user on the create profiles screen "{create_profiles_url}"')
# def step_impl(context, create_profiles_url):
#     context.onboarding_provider_page.check_create_profiles_url(create_profiles_url)
#
# @When("accountprovider: I click on add member button to open the add team member modal")
# def step_impl(context):
#     context.onboarding_provider_page.click_add_team_member()
#
# @When('accountprovider: I fill in the first name "{members_first_name}"')
# def step_impl(context, members_first_name):
#     context.onboarding_provider_page.input_member_first_name(members_first_name)
#
# @When('accountprovider: I fill in the last name "{members_last_name}"')
# def step_impl(context, members_last_name):
#     context.onboarding_provider_page.input_member_last_name(members_last_name)
#
# @When('accountprovider: I fill in the email address "{members_email}"')
# def step_impl(context, members_email):
#     context.onboarding_provider_page.input_member_email(members_email)
#
# @When('accountprovider: I fill in the Job title field "{members_job_title}"')
# def step_impl(context, members_job_title):
#     context.onboarding_provider_page.input_member_job_title(members_job_title)
#
# @Then("accountprovider: Click on add button from the modal")
# def step_impl(context):
#     context.onboarding_provider_page.click_add_btn_from_modal()
#
# @Then("accountprovider: Click on continue button to send the invites to the added members")
# def step_impl(context):
#     context.onboarding_provider_page.click_continue_from_add_member_screen()