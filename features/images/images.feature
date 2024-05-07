@images
Feature: Images

  @acceptance
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that get all images endpoint return all the images created

    When I call to "images" endpoint using "GET" option and with parameters
    Then I receive the response and validate with "get_all_images" file
    And I validate the status code is 200


  @create
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that create image endpoint return a image created
    As I user I want to create a image in The Cat API

    When I call to "images" endpoint using "POST" option and with parameters
    Then I receive the response and validate with "upload_image" file
    And I validate the status code is 201

  @image_id  @acceptance
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that delete image endpoint deletes the image
    As I user I want to delete a image in The Cat API

    When I call to "images" endpoint using "DELETE" option and with parameters
    Then I receive the response and validate with "delete_image" file
    And I validate the status code is 204
