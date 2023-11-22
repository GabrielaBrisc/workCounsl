Feature: Check the sign in functionality
  @signin
  Scenario: Enter valid email address and password
    Given signIn: I am a user on the sign in page
    When signIn: I fill in the email field with valid address "gabriela.brisc+test1@saltandpepper.co"
    When signIn: I click outside
    When signIn: I fill in the password field with valid pass "Mypass1*"
    When signIn: I click outside again
    Then signIn: I click on continue button from login screen
    Then signIn: I verify the url "https://staging.counsl.dev/dashboard"

