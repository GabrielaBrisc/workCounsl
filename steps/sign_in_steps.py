from behave import  *

@Given("signIn: I am a user on the sign in page")
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in()

@When('signIn: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.sign_in_page.input_email_address(email_address)

@When('signIn: I click outside')
def step_impl(context):
    context.sign_in_page.click_outside_field()

@When('signIn: I fill in the password field with valid pass "{password}"')
def step_impl(context, password):
    context.sign_in_page.input_password(password)

@When('signIn: I click outside again')
def step_impl(context):
    context.sign_in_page.click_outside_field2()

@Then("signIn: I click on continue button from login screen")
def step_impl(context):
    context.sign_in_page.click_continue_btn()

@Then('signIn: I verify the url "{dashboard_url}"')
def step_impl(context, dashboard_url):
    context.sign_in_page.check_the_current_url(dashboard_url)