Feature: Product Page
  Background: Open login page
    Given Currently i am on the product page



  @smoke
  Scenario: Check if the URL is correct
    Given Now i am on the login page
    Then The current of the page is "https://www.saucedemo.com/v1/"

  @regression
  Scenario: Check the if the email and password are correct
    Given I am on the login page
    When I put right email
    And I put right password
    And I access the login button
    Then The URL of the product page is "https://www.saucedemo.com/v1/inventory.html"


    @regression
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

      @regression
      Scenario: Cart page
        Given Located in the login page
        When I press the right email
        And I press  the right password
        And I enter the login button
        And The product page URL is "https://www.saucedemo.com/v1/inventory.html"
        When I click the cart button
        Then I should see "https://www.saucedemo.com/v1/cart.html"



        @regression
        Scenario: Cart page CHECKOUT button
          Given Present on the login page
          When I write my correct email
          And I write my correct password
          And I click the login function
          And The product page URL is correct "https://www.saucedemo.com/v1/inventory.html"
          And I press the cart button
          And I have to see "https://www.saucedemo.com/v1/cart.html"
          And I press the CHECKOUT button
          Then I should see the Checkout information page "https://www.saucedemo.com/v1/checkout-step-one.html"



         @regression
          Scenario:
            Given I press the login button
            When I enter correct username
            And I enter correct password
            And I click the button
            And I add product to cart
            And I click the cart
            And I click checkout button
            And I enter First Name
            And I enter Last Name
            And I enter zip postal code
            And I click the continue button
            And I click finish button
            Then I see "Your order has been dispatched, and will arrive just as fast as the pony can get there!"


           @regression
           Scenario:
             Given I access the login button
             When I introduce the correct email
             And I introduce the correct password
             And I press the access button
             And I put the product in to the cart
             And I access the cart
             Then I click the remove from cart button


