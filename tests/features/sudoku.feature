Feature: Sudoku Solver
  Scenario: Solving a fully solvable Sudoku puzzle
    Given a fully solvable Sudoku board
    When the solver attempts to solve the board
    Then the board should be solved correctly

  Scenario: Attempting to solve an unsolvable Sudoku puzzle
    Given an unsolvable Sudoku board
    When the solver attempts to solve the board
    Then the solver should indicate the puzzle is unsolvable

