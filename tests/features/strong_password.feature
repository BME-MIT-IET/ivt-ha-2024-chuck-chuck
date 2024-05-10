Feature: Strong Password Validation
  As a user signing up on the website
  I want to ensure my password is strong
  So that my account is secure

  Scenario Outline: Check if a password is strong
    Given a password of length "<length>" and content "<password>"
    When I check if the password is strong
    Then I should be told to add "<needed_chars>" more characters to make it strong

    Examples:
      | length | password     | needed_chars |
      | 3      | Ab1          | 3            |
      | 11     | #Algorithms  | 1            |
