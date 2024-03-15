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


      Scenario Outline:
        Given Present on the login page
        When I push "<username>" email
        And I push "<password>" password
        And I push the login button
        And The product page URL is "https://www.saucedemo.com/v1/inventory.html"
        And I push Add to cart
        And I navigate to page "https://www.saucedemo.com/v1/cart.html"
        And I click remove button
        Then I should see no product in the cart

        Examples:
         | username          | password       |
         | standard_user     | secret_sauce   |
