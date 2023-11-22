Feature: As provider, I want to add a draft service

  @adddraftservice
  Scenario: I sign in as provider to Counsl
    Given addDraftService: I am a user on the sign in page
    When addDraftService: I fill in the email field with valid address "gabriela.brisc+testp1@saltandpepper.co"
    When addDraftService: I click outside
    When addDraftService: I fill in the password field with valid pass "Mypass1*"
    When addDraftService: I click outside again
    Then addDraftService: I click on continue button from login screen

  @adddraftservice
  Scenario: I go to service page and add a draft service
    Given addDraftService: I am a provider on dashboard screen "https://staging.counsl.dev/dashboard"
    When addDraftService: I click on Service left side menu
    Then addDraftService: I click on the add service button
    When addDraftService: The modal was opened and I fill the service name field "QA"
    When addDraftService: I fill the service type field "IT"
    When addDraftService: I fill the tags field "testing types"
    Then addDraftService: I hit enter to add the tag
    When addDraftService: I add the details about the service into about field "I offer testing services"
    #oare la img ar trebui sa adaug si acel link spre poza?
    When addDraftService: I add the image cover into image cover field
    When addDraftService: I select the draft status by clicking on the Draft radio btn
    Then addDraftService: I verify if save button is displayed
    Then addDraftService: I click on the Save btn to save the draft service and the modal is closed
    #as putea verifica daca modala mai e afisata? fol locator al acelei modale si sa pun ca e enabled or disabled

