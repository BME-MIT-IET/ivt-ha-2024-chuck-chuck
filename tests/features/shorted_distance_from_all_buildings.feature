Feature: Shortest Distance to All Buildings
  Scenario: Grid with multiple buildings and empty spaces
    Given a grid with buildings and empty spaces
    When calculating the shortest distance to all buildings
    Then the shortest distance should be calculated correctly


  Scenario: Grid with no empty spaces
    Given a grid with buildings but no empty spaces
    When calculating the shortest distance to all buildings
    Then the result should be -1 as there are no empty spaces
