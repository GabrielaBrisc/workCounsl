Feature: As provider, I want to add a draft service

  @adddpublicservice
  Scenario: I sign in as provider to Counsl
    Given addPublicService: I am a user on the sign in page
    When addPublicService: I fill in the email field with valid address "gabriela.brisc+testp1@saltandpepper.co"
    When addPublicService: I click outside
    When addPublicService: I fill in the password field with valid pass "Mypass1*"
    When addPublicService: I click outside again
    Then addPublicService: I click on continue button from login screen

  @adddpublicservice
  Scenario: I go to service page and add a draft service
    Given addPublicService: I am a provider on dashboard screen "https://staging.counsl.dev/dashboard"
    When addPublicService: I click on Service left side menu
    Then addPublicService: I click on the add service button
    When addPublicService: The modal was opened and I fill the service name field "QA"
    When addPublicService: I fill the service type field "IT"
    When addPublicService: I fill the tags field "testing types"
    Then addPublicService: I hit enter to add the tag
    When addPublicService: I add the details about the service into about field "I offer testing services"
    #oare la img ar trebui sa adaug si acel link spre poza?
    When addPublicService: I add the image cover into image cover field
    Then addPublicService: I click on the Save btn to save the draft service and the modal is closed
    Then addPublicService: I verift the public services list

