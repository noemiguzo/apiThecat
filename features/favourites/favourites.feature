
@favourites
Feature: Favourites

  # Title of test case
  @allure.label.owner:Noemi_Guzman
  @acceptance
  Scenario: Verify that get all favourites endpoint return all the favourites created

    When I call to "favourites" endpoint using "GET" option and with parameters
    Then I receive the response and validate with "get_all_favourites" file
    And I validate the status code is 200


  @favourite_id  @create
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that create vote endpoint return a vote created
    As I user I want to create a project in CAT API

    When I call to "favourites" endpoint using "POST" option and with parameters
    Then I receive the response and validate with "create_favourite" file
    And I validate the status code is 200

  @favourite_id  @delete
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that delete image endpoint deletes the project
    As I user I want to delete a image in CAT API

    When I call to "favourites" endpoint using "DELETE" option and with parameters
    Then I receive the response and validate with "delete_favourite" file
    And I validate the status code is 200
