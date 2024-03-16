Feature: Product Page
  Background: Open login page
    Given Currently i am on the product page



  @smoke
  Scenario: Check if the URL is correct
    Given Now i am on the login page
    Then The current of the page is "https://www.saucedemo.com/v1/"

  @regression
  Scenario Outline: Check the if the email and password are correct
    Given I am on the login page
    When I put "<username>" email
    And I put "<password>" password
    And I access the login button
    Then The URL of the product page is "https://www.saucedemo.com/v1/inventory.html"
    Examples:
         | username          | password       |
         | standard_user     | secret_sauce   |


    Scenario Outline: Add to cart
      Given Located on the login page
      When I introduce "<username>" email
      And I introduce "<password>" password
      And I press the login button
      And The URL of the product page is "https://www.saucedemo.com/v1/inventory.html"
      And I click Add to cart
      Then Cart has "1" item in it
      Examples:
         | username          | password       |
         | standard_user     | secret_sauce   |


      Scenario Outline: Cart page
        Given Located in the login page
        When I press "<username>" email
        And I press  "<password>" password
        And I enter the login button
        And The product page URL is "https://www.saucedemo.com/v1/inventory.html"
        When I click the cart button
        Then I should see "https://www.saucedemo.com/v1/cart.html"

        Examples:
         | username          | password       |
         | standard_user     | secret_sauce   |

        Scenario Outline: Cart page CHECKOUT button
          Given Present on the login page
          When I write my "<username>" email
          And I write my "<password>" password
          And I click the login function
          And The product page URL is correct "https://www.saucedemo.com/v1/inventory.html"
          And I press the cart button
          And I have to see "https://www.saucedemo.com/v1/cart.html"
          And I press the CHECKOUT button
          Then I should see the Checkout information page "https://www.saucedemo.com/v1/checkout-step-one.html"

          Examples:
         | username          | password       |
         | standard_user     | secret_sauce   |