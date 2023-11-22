Feature: Check the sign in functionality

  @signin_invalid
  Scenario: Enter valid email address and password
    Given signIn_invalid: I am a user on the sign in page
    When signIn_invalid: I fill in the email field with valid address "gabriela.brisc+new@saltandpepper.co"
    When signIn_invalid: I click outside
      When signIn_invalid: I verify the invalid text "Invalid email"
    When signIn_invalid: I fill in the password field with valid pass "Mypass1*"
    When signIn_invalid: I click outside again
    Then signIn_invalid: I click on continue button from login screen
    Then signIn_invalid: I verify the url "https://staging.counsl.dev/dashboard"
