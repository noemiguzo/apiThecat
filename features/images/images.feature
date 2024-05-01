@images
Feature: Images

  # Title of test case
  @acceptance
  Scenario: Verify that get all images endpoint return all the images created

    When I call to "images" endpoint using "GET" option and with parameters
    Then I receive the response and validate with "get_all_images" file
    And I validate the status code is 200


  @create
  Scenario: Verify that create project endpoint return a project created
    As I user I want to create a project in TODOIST API

    When I call to "images" endpoint using "POST" option and with parameters
    Then I receive the response and validate with "upload_image" file
    And I validate the status code is 201

  @image_id  @acceptance
  Scenario: Verify that delete image endpoint deletes the project
    As I user I want to delete a image in TODOIST API

    When I call to "images" endpoint using "DELETE" option and with parameters
    Then I receive the response and validate with "delete_image" file
    And I validate the status code is 204
