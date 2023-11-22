from behave import *

#  Scenario: I sign in as consumer to check the left side menus
@Given("navigate_menus: I am a consumer on the sign in page")
def step_impl(context):
    context.navigate_menus_page.navigate_to_sign_in()

@When('navigate_menus: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.navigate_menus_page.input_email_address(email_address)

@When('navigate_menus: I click outside')
def step_impl(context):
    context.navigate_menus_page.click_outside_field()

@When('navigate_menus: I fill in the password field with valid pass "{password}"')
def step_impl(context, password):
    context.navigate_menus_page.input_password(password)

@When('navigate_menus: I click outside again')
def step_impl(context):
    context.navigate_menus_page.click_outside_field2()

@Then("navigate_menus: I click on continue button from login screen")
def step_impl(context):
    context.navigate_menus_page.click_continue_btn()


#  Scenario: As a user, I want to navigate through left side menus
@Given('navigate_menus: I am a provider on the Dashboard screen "{dashboard_url}"')
def step_impl(context, dashboard_url):
    context.navigate_menus_page.check_the_dashboard_url(dashboard_url)

@When("navigate_menus: I click on Search Services menu")
def step_impl(context):
    context.navigate_menus_page.navigate_to_services()

@When("navigate_menus: I click on the checkbox from Search System modal")
def step_impl(context):
    context.navigate_menus_page.click_checkbox_search_system()

@Then("navigate_menus: I click on Cancel button from Search System modal")
def step_impl(context):
    context.navigate_menus_page.click_cancel_btn_search_system()

@Then('navigate_menus: I verify the search services url "{search_url}"')
def step_impl(context, search_url):
    context.navigate_menus_page.check_the_search_services_url(search_url)

@When("navigate_menus: I click on the Messages menu")
def step_impl(context):
    context.navigate_menus_page.navigate_to_messages()

@Then('navigate_menus: I verify the message menu url "{messages_url}"')
def step_impl(context,messages_url):
    context.navigate_menus_page.check_the_messages_url(messages_url)

@When("navigate_menus: I click on Team menu")
def step_impl(context):
    context.navigate_menus_page.navigate_to_team()

@Then('navigate_menus: I verify the team menu url "{team_url}"')
def step_impl(context, team_url):
    context.navigate_menus_page.check_the_teams_url(team_url)

@When("navigate_menus: I click on appointments menu")
def step_impl(context):
    context.navigate_menus_page.navigate_to_appointments()

@Then('navigate_menus: I verify the appointments url "{appointments_url}"')
def step_impl(context, appointments_url):
    context.navigate_menus_page.check_the_appointments_url(appointments_url)

@When("navigate_menus: I click on Wallet menu")
def step_impl(context):
    context.navigate_menus_page.navigate_to_wallet()

@Then('navigate_menus: I verify the wallet url "{wallet_url}"')
def step_impl(context, wallet_url):
    context.navigate_menus_page.check_the_wallet_url(wallet_url)

@When("navigate_menus: I click on Settings menu")
def step_impl(context):
    context.navigate_menus_page.navigate_to_settings()

@Then('navigate_menus: I verify the settings url "{settings_url}"')
def step_impl(context, settings_url):
    context.navigate_menus_page.check_the_settings_url(settings_url)






