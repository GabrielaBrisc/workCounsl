Feature: Check the left-side menus

  @leftmenus
  Scenario: I sign in as consumer to check the left side menus
    Given navigate_menus: I am a consumer on the sign in page
    When navigate_menus: I fill in the email field with valid address "gabriela.brisc+test1@saltandpepper.co"
    When navigate_menus: I click outside
    When navigate_menus: I fill in the password field with valid pass "Mypass1*"
    When navigate_menus: I click outside again
    Then navigate_menus: I click on continue button from login screen

  @leftmenus
  Scenario: As a user, I want to navigate through left side menus
    Given navigate_menus: I am a provider on the Dashboard screen "https://staging.counsl.dev/dashboard"
    When navigate_menus: I click on Search Services menu
    When navigate_menus: I click on the checkbox from Search System modal
    Then navigate_menus: I click on Cancel button from Search System modal
    Then navigate_menus: I verify the search services url "https://staging.counsl.dev/service-search"
    When navigate_menus: I click on the Messages menu
    Then navigate_menus: I verify the message menu url "https://staging.counsl.dev/messages"
    When navigate_menus: I click on Team menu
    Then navigate_menus: I verify the team menu url "https://staging.counsl.dev/team"
    When navigate_menus: I click on appointments menu
    Then navigate_menus: I verify the appointments url "https://staging.counsl.dev/appointments"
    When navigate_menus: I click on Wallet menu
    Then navigate_menus: I verify the wallet url "https://staging.counsl.dev/wallet"
    When navigate_menus: I click on Settings menu
    Then navigate_menus: I verify the settings url "https://staging.counsl.dev/settings"


