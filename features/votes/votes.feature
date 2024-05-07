@votes
Feature: Votes

  @image_id  @acceptance
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that get all votes endpoint return all the votes created

    When I call to "votes" endpoint using "GET" option and with parameters
    Then I receive the response and validate with "get_all_votes" file
    And I validate the status code is 200

  @image_id  @create
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that create vote endpoint return a vote created
    As I user I want to create a vote The Cat API

    When I call to "votes" endpoint using "POST" option and with parameters
    Then I receive the response and validate with "post_a_vote" file
    And I validate the status code is 201

  @vote_id  @delete
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify that delete image endpoint deletes the Vote
    As I user I want to delete a image in The Cat API

    When I call to "votes" endpoint using "DELETE" option and with parameters
    Then I receive the response and validate with "delete_vote" file
    And I validate the status code is 200

  @image_id  @parse
  @allure.label.owner:Noemi_Guzman
  Scenario:   Verify I can create a vote in CAT API
    When I create a vote "Vote created using data type" in CAT API
    Then I validate the status code is 201

  @image_id  @parse
  @allure.label.owner:Noemi_Guzman
  Scenario: Verify I can create multiple Votes
    When I create a vote "<sub_id><value>" in CAT API
    | sub_id    |  value |
    | homework  | 2 |
    | dinner    | 1 |
    | bank      | 3 |
