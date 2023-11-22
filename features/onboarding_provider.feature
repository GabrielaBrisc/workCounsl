Feature: Check the onboarding provider functionality

  @onboardingprovider
  Scenario: I want to choose between the 2 options from create account screen
    Given accountprovider: I am a user on the create account first screen
    Then accountprovider: I click on Offer Services button
#
   @onboardingprovider
#  Scenario: Enter the credentials to create the account
#     Given accountprovider: I am a user on the create account second screen "https://staging.counsl.dev/provider/signup"
#     When accountprovider: I fill in the email field with valid address "gabriela.brisc+test@saltandpepper.co"
#     When accountprovider: I fill in the password field "Mypass1*"
#     When accountprovider: I fill in the confirm password field "Mypass1*"
#     When accountprovider: I click on the checkbox to agree with terms and policy
#     Then accountprovider: I click on the Sign Up button

   @onboardingprovider
#  Scenario:
#     When accountprovider: I clear the input field
#     When accountprovider: I input the companies house no. "14786848"
#     Then accountprovider: I click on Continue button
#
#     # cum sa adaug o poza pe screen-ul cu company logo
   @onboardingprovider
#  Scenario: Add the company logo
#    When accountprovider: I upload the logo
#    Then accountprovider: I click on Continue button
#
   @onboardingprovider
#  Scenario: Fill in all the fields from Create a company third screen
#    Given accountprovider: I am a user on the Make a personal profile screen "https://staging.counsl.dev/provider/create-company/personal-profile"
#    When accountprovider: I input the first name "Gabriela"
#    When accountprovider: I input the last name "Brisc"
#    When accountprovider: I input the user title "Admin"
#    Then accountprovider: I click on Continue button from Make a personal profile screen

   @onboardingprovider
#  Scenario: Fill in the credit cards details
#    When accountprovider: I input the email field "gabriela.brisc@saltandpepper.co"
#    When accountprovider: I input the credit number field "4242424242424242"
#    When accountprovider: I input the month and year field "1125"
#    When accountprovider: I input the CVC field "123"
#    When accountprovider: I input the name on card "test"
#    Then accountprovider: I click on the Payment button

    @onboardingprovider
#  Scenario: Click on Continue button from Payment successful screen
#    Given accountprovider: I am a user on the Payment successful screen "https://staging.counsl.dev/provider/become-member/success"
#    Then accountprovider: I click on Continue button
#
# de vazut cum fac cand nu stiu cati directori am si cum fac fill in la emails

    @onboardingprovider
#  Scenario: Fill in the directors email
#    Given accountprovider: I am a user on the Verify your business screen "https://staging.counsl.dev/provider/verify-business"
#    When accountprovider: I click on add email button
#    When accountprovider: I fill in the email field "gabriela.brisc+directorp@saltandpepper.co"
#    Then accountprovider: Click on add button
  #  Then accountprovider: Click on continue and send verification emails button

#    #ar trebui sa verific daca mai sunt directori
#  #la care trebuie sa adaug email
#
    @onboardingprovider
#   Scenario: Add a team member
#     Given accountprovider: I am a user on the create profiles screen "https://staging.counsl.dev/provider/team-and-services/create-profiles"
#     #pt provider:
#     #cum ar trebui sa fac daca adaug 5 membrii,
#        # sa verific daca apare buy slot member
#     #si sa vad ca mai pot adauga membrii dupa ce cumpar acel slot?
#     #cum ma duc pe acel flow?
#     #pot sa adaug 5 useri, verif ca apare buy member slot
#     #dupa care adaug member slot si mai adaug membru
#     #dar daca as avea mai multe teste pe acest screen si deja as fi adaugat un membru
#     #eu trebe sa verif daca am 5 sau nu, nu sa ii adaug direct 5
#     When accountprovider: I click on add member button to open the add team member modal
#     Then accountprovider: I fill in the first name "Team"
#     Then accountprovider: I fill in the last name "Member"
#     Then accountprovider: I fill in the email address "gabriela.brisc+member11@saltandpepper.co"
#     Then accountprovider: I fill in the Job title field "Admin"
#     Then accountprovider: Click on add button
#     Then accountprovider: Click on continue and send invites button
#
    @onboardingprovider
##  Scenario: Delete an added team member
##    Given accountprovider: I am a user on the create profiles screen
##    When accountprovider: I check if there is an added member
##    When accountprovider: I click on the three dots
##    Then accountprovider: I click on Delete button

    @onboardingprovider
#  Scenario: I add the first service
#    When accountprovider: I fill in the service name "
#    When accountprovider: I fill in the service type
#    When accountprovider: I click on the tier dropdown field
#    When accountprovider: I select the tier2 from the dropdown
#    When accountprovider: I input a tag name <test> and hit enter
#    When accountprovider: I input the service description <testing>
#    When accountprovider: I click on upload file
#    When accountprovider: I select the image cover
#    Then accountprovider: I click on save to draft button

    @onboardingprovider
#  Scenario: I set the availability
#    When accountprovider: I verify the url
#    Then accountprovider: I click on save button from the availability modal

#    #scenario to test the settings and to check if the left side menus are enabled





