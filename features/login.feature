Feature: Login Page

  Background: Open login page
    Given Currently i am on the login page



  @smoke
  Scenario: Check if the URL is correct
    Given Currently i am on the login page
    Then The URL of the page is "https://www.saucedemo.com/v1/"

  @regression
   Scenario Outline: Trying to login with wrong email
     Given Currently i am on the login page
     When I enter "<username>" email
     And I enter "<password>" password
     And I click the login button
     Then I have to see "Epic sadface: Username and password do not match any user in this service"
     Examples:
         | username          | password       |
         | dori9@gmail.com   | 12345678       |
         | pyta9@yahoo.com   | 07566723547623 |
         | google.@gmail.com | ieyrghjklcvb   |


    @regresion
    Scenario Outline: Trying to login with right email and password
     Given Currently i am on the login page
     When I enter "<username>" email
     And I enter "<password>" password
     And I click the login button
      Examples:
         | username          | password       |
         | standard_user     | secret_sauce   |
