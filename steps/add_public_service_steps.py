from behave import  *

@Given("addPublicService: I am a user on the sign in page")
def step_impl(context):
    context.add_public_service_page.navigate_to_sign_in()

@When('addPublicService: I fill in the email field with valid address "{email_address}"')
def step_impl(context, email_address):
    context.add_public_service_page.input_email_address(email_address)

@When('addPublicService: I click outside')
def step_impl(context):
    context.add_public_service_page.click_outside_field()

@When('addPublicService: I fill in the password field with valid pass "{password}"')
def step_impl(context, password):
    context.add_public_service_page.input_password(password)

@When('addPublicService: I click outside again')
def step_impl(context):
    context.add_public_service_page.click_outside_field2()

@Then("addPublicService: I click on continue button from login screen")
def step_impl(context):
    context.add_public_service_page.click_continue_btn()


#  Scenario: I go to service page and add a draft service
@Given('addPublicService: I am a provider on dashboard screen "{dashboard_url}"')
def step_impl(context, dashboard_url):
    context.add_public_service_page.check_the_dashboard_url(dashboard_url)

@When("addPublicService: I click on Service left side menu")
def step_impl(context):
    context.add_public_service_page.click_on_service_left_menu()

@Then("addPublicService: I click on the add service button")
def step_impl(context):
    context.add_public_service_page.click_add_service_btn()

@When('addPublicService: The modal was opened and I fill the service name field "{service_name}"')
def step_impl(context, service_name):
    context.add_public_service_page.input_service_name(service_name)

@When('addPublicService: I fill the service type field "{service_type}"')
def step_impl(context, service_type):
    context.add_public_service_page.input_service_type(service_type)

@When('addPublicService: I fill the tags field "{tags}"')
def step_impl(context, tags):
    context.add_public_service_page.input_tags(tags)

@Then("addPublicService: I hit enter to add the tag")
def step_impl(context):
    context.add_public_service_page.hit_enter_tags()

#oare la poza ar trebui sa adaug si un parametru?
@When('addPublicService: I add the details about the service into about field "{about_field}"')
def step_impl(context, about_field):
    context.add_public_service_page.input_about_service_details(about_field)

@When("addPublicService: I add the image cover into image cover field")
def step_impl(context):
    context.add_public_service_page.upload_image_cover()

#the public radio btn is selected by default

@Then("addPublicService: I click on the Save btn to save the draft service and the modal is closed")
def step_impl(context):
    context.add_public_service_page.click_save_service_btn()

@Then("addPublicService: I verift the public services list")
def step_impl(context):
    context.add_public_service_page.verify_the_no_of_services()






