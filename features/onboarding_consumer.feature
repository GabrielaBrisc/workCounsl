#Feature: Check the onboarding functionality
#
#  @onboarding
#  Scenario: I want to choose between the 2 options from create account screen
#    Given onboarding: I am a user on the create account first screen
#    Then onboading: I click on Find Professionals button
#  @onboarding
#  Scenario: Enter the credentials to create the account
#     Given onboarding: I am a user on the create account second screen "https://staging.counsl.dev/consumer/signup"
#     When onboarding: I fill in the email field with valid address "gabriela.brisc+test20@saltandpepper.co"
#     When onboarding: I fill in the password field "Mypass1*"
#     When onboarding: I fill in the confirm password field "Mypass1*"
#     When onboarding: I click on the checkbox to agree with terms and policy
#     Then onboarding: I click on the Sign Up button
#
#  @onboarding
#  Scenario: Input company house no. on the Create a company screen
##    Given onboarding: I am a user on the Create a company screen "https://staging.counsl.dev/consumer/create-company/address"
#    When onboarding: I clear the input field
#    Then onboarding: I input the companies house no. "14586854"
#    Then onboarding: I click on Continue button from create company first screen
#
#  @onboarding
##     # cum sa adaug o poza pe screen-ul cu company logo
#  Scenario: Add the company logo
##    When onboarding: I click on Upload button
#    When onboarding: I upload the logo
#    Then onboarding: I click on Continue button from add logo screen

#    @onboarding
##  Scenario: Fill in all the fields from Create a company third screen
#    Given onboarding: I am a user on the Make a personal profile screen "https://staging.counsl.dev/consumer/create-company/personal-profile"
#    When onboarding: I input the first name "Gabriela"
#    When onboarding: I input the last name "Brisc"
#    When onboarding: I input the job title "Admin"
#    Then onboarding: I click on Continue button from Make a personal profile screen
#
#  @onboarding
#  Scenario: Fill in all the fields from Tell Us About Your Business screen
#    Given onboarding: I am a user on the Tell Us About Your Business screen "https://staging.counsl.dev/consumer/create-company/business-details"
#    When onboarding: I fill in the company size field "2"
#    When onboarding: I fill in the Tell Us About Your Company field "My company is an outsourcing company"
#    When onboarding: I fill in the What is the most pressing problem you are having today? field "I have problems with management"
#    Then onboarding: I click on continue button from Tell Us About Your Business screen
##

#  @onboarding
#  Scenario: Choose the basic plan
#    Given onboarding: I am a user on the Plans screen "https://staging.counsl.dev/consumer/become-member"
#    Then onboarding: I click on the desired plan
#
  @onboarding
#  Scenario: Fill in the credit cards details from stripe
#    When onboarding: I input the email field "gabriela.brisc@saltandpepper.co"
#    When onboarding: I input the card number field "4242424242424242"
#    When onboarding: I input the month and year field "1125"
#    When onboarding: I input the CVC field "123"
#    When onboarding: I input the name on card "test"
#    Then onboarding: I click on the Payment button
#
    @onboarding
#  Scenario: Click on Continue button from Payment successful screen
#    Given onboarding: I am a user on the Payment successful screen "https://staging.counsl.dev/consumer/become-member/success"
#    Then onboarding: I click on Continue button from payment successful
#
#
#  ###cum fac cand am mai multi directori? asta daca nu as sti la company house cati directori sunt

    @onboarding
#  Scenario: Fill in the directors email
#    Given onboarding: I am a user on the Verify your business screen "https://staging.counsl.dev/consumer/verify-business"
#    When onboarding: I click on add email button
#    When onboarding: I fill in the email field "gabriela.brisc+director@saltandpepper.co"
#    Then onboarding: Click on add button and the modal is closed
#    Then onboarding: I click on the Continue and Send Verification Emails btn
##    #ar trebui sa verific daca mai sunt directori
##  #la care trebuie sa adaug email

    @onboarding
#   Scenario: Add a team member
#     Given onboarding: I am a user on the create profiles screen "https://staging.counsl.dev/consumer/team-and-services/create-profiles"
#     When onboarding: I click on add member button to open the add team member modal
#     When onboarding: I fill in the first name "Team"
#     When onboarding: I fill in the last name "Member"
#     When onboarding: I fill in the email address "gabriela.brisc+member9@saltandpepper.co"
#     When onboarding: I fill in the Job title field "Admin"
#     Then onboarding: Click on add button from the modal
#     #de verificat
##     When onboarding: The modal is closed and the member is added
#     Then onboarding: Click on continue button to send the invites to the added members
#
#
#  # cum adaug mai multi team members? pot cu pasii prin care l am adaugat pe primul, sa mai adaug?
#
#
##    #scenario to test the settings and to check if the left side menus are enabled
#
#
#
#
#
