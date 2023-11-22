from behave import *

#  Scenario: I sign in as consumer
@Given("consumerSignIn: I am a consumer on the sign in page")
def step_impl(context):
    context.search_service_page.navigate_to_sign_in()

@When('consumerSignIn: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.search_service_page.input_email_address(email_address)

@When('consumerSignIn: I click outside')
def step_impl(context):
    context.search_service_page.click_outside_field()

@When('consumerSignIn: I fill in the password field with valid pass "{password}"')
def step_impl(context, password):
    context.search_service_page.input_password(password)

@When('consumerSignIn: I click outside again')
def step_impl(context):
    context.search_service_page.click_outside_field2()

@Then("consumerSignIn: I click on continue button from login screen")
def step_impl(context):
    context.search_service_page.click_continue_btn()


#  Scenario: I am a consumer on the search screen and I search for a service

@Given("searchservice: I am a consumer on the search screen")
def step_impl(context):
    context.search_service_page.navigate_to_service_search()

@When("searchservice: I click on the checkbox from Search System modal")
def step_impl(context):
    context.search_service_page.click_checkbox_search_system()

@Then("searchservice: I click on Cancel button from Search System modal")
def step_impl(context):
    context.search_service_page.click_cancel_btn_search_system()

@When('searchservice: I input the search details into search field "{search_details}"')
def step_impl(context, search_details):
    context.search_service_page.input_search_details(search_details)

@Then("searchservice: I click on the submit search button")
def step_impl(context):
    context.search_service_page.click_submit_search_btn()