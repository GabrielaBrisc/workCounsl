Feature: Check the search functionality
  @searchtest
  Scenario: I sign in as consumer
    Given consumerSignIn: I am a consumer on the sign in page
    When consumerSignIn: I fill in the email field with valid address "gabriela.brisc+test1@saltandpepper.co"
    When consumerSignIn: I click outside
    When consumerSignIn: I fill in the password field with valid pass "Mypass1*"
    When consumerSignIn: I click outside again
    Then consumerSignIn: I click on continue button from login screen

  @searchtest
  Scenario: I am a consumer on the search screen and I search for a service
    Given searchservice: I am a consumer on the search screen
    When searchservice: I click on the checkbox from Search System modal
    Then searchservice: I click on Cancel button from Search System modal
    When searchservice: I input the search details into search field "management"
    Then searchservice: I click on the submit search button