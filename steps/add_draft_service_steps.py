from behave import  *

@Given("addDraftService: I am a user on the sign in page")
def step_impl(context):
    context.add_draft_service_page.navigate_to_sign_in()

@When('addDraftService: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.add_draft_service_page.input_email_address(email_address)

@When('addDraftService: I click outside')
def step_impl(context):
    context.add_draft_service_page.click_outside_field()

@When('addDraftService: I fill in the password field with valid pass "{password}"')
def step_impl(context, password):
    context.add_draft_service_page.input_password(password)

@When('addDraftService: I click outside again')
def step_impl(context):
    context.add_draft_service_page.click_outside_field2()

@Then("addDraftService: I click on continue button from login screen")
def step_impl(context):
    context.add_draft_service_page.click_continue_btn()


#  Scenario: I go to service page and add a draft service
@Given('addDraftService: I am a provider on dashboard screen "{dashboard_url}"')
def step_impl(context, dashboard_url):
    context.add_draft_service_page.check_the_dashboard_url(dashboard_url)

@When("addDraftService: I click on Service left side menu")
def step_impl(context):
    context.add_draft_service_page.click_on_service_left_menu()

@Then("addDraftService: I click on the add service button")
def step_impl(context):
    context.add_draft_service_page.click_add_service_btn()

@When('addDraftService: The modal was opened and I fill the service name field "{service_name}"')
def step_impl(context, service_name):
    context.add_draft_service_page.input_service_name(service_name)

@When('addDraftService: I fill the service type field "{service_type}"')
def step_impl(context, service_type):
    context.add_draft_service_page.input_service_type(service_type)

@When('addDraftService: I fill the tags field "{tags}"')
def step_impl(context, tags):
    context.add_draft_service_page.input_tags(tags)

@Then("addDraftService: I hit enter to add the tag")
def step_impl(context):
    context.add_draft_service_page.hit_enter_tags()

#oare la poza ar trebui sa adaug si un parametru?
@When('addDraftService: I add the details about the service into about field "{about_field}"')
def step_impl(context, about_field):
    context.add_draft_service_page.input_about_service_details(about_field)

@When("addDraftService: I add the image cover into image cover field")
def step_impl(context):
    context.add_draft_service_page.upload_image_cover()

@When("addDraftService: I select the draft status by clicking on the Draft radio btn")
def step_impl(context):
    context.add_draft_service_page.select_draft_radio_btn()

@Then("addDraftService: I verify if save button is displayed")
def step_impl(context):
    context.add_draft_service_page.test_element_not_displayed_v1()


@Then("addDraftService: I click on the Save btn to save the draft service and the modal is closed")
def step_impl(context):
    context.add_draft_service_page.click_save_service_btn()





