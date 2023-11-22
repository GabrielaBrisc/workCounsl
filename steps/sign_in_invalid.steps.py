from behave import  *

@Given("signIn_invalid: I am a user on the sign in page")
def step_impl(context):
    context.sign_in_invalid_page.navigate_to_sign_in()

@When('signIn_invalid: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.sign_in_invalid_page.input_email_address(email_address)

@When('signIn_invalid: I click outside')
def step_impl(context):
    context.sign_in_invalid_page.click_outside_field()

@When('signIn_invalid: I verify the invalid text "{error_message}"')
def step_impl(context, error_message):
    context.sign_in_invalid_page.check_displayed_message(error_message)

@When('signIn_invalid: I fill in the password field with valid pass "{password}"')
def step_impl(context, password):
    context.sign_in_invalid_page.input_password(password)

@When('signIn_invalid: I click outside again')
def step_impl(context):
    context.sign_in_invalid_page.click_outside_field2()

@Then("signIn_invalid: I click on continue button from login screen")
def step_impl(context):
    context.sign_in_invalid_page.click_continue_btn()

@Then('signIn_invalid: I verify the url "{dashboard_url}"')
def step_impl(context, dashboard_url):
    context.sign_in_invalid_page.check_the_current_url(dashboard_url)