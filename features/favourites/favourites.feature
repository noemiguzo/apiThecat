
@favourites
Feature: Favourites

  # Title of test case
  @acceptance
  Scenario: Verify that get all favourites endpoint return all the favourites created

    When I call to "favourites" endpoint using "GET" option and with parameters
    Then I receive the response and validate with "get_all_favourites" file
    And I validate the status code is 200


  @favourite_id  @create
  Scenario: Verify that create vote endpoint return a vote created
    As I user I want to create a project in TODOIST API

    When I call to "favourites" endpoint using "POST" option and with parameters
    Then I receive the response and validate with "create_favourite" file
    And I validate the status code is 200

  @favourite_id  @delete
  Scenario: Verify that delete image endpoint deletes the project
    As I user I want to delete a image in TODOIST API

    When I call to "favourites" endpoint using "DELETE" option and with parameters
    Then I receive the response and validate with "delete_favourite" file
    And I validate the status code is 200
