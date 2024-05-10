from behave import *

from algorithms.dfs import Sudoku


# Context setup for a fully solvable board
@given('a fully solvable Sudoku board')
def step_impl(context):
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    context.sudoku = Sudoku(board, 9, 9)

# Context setup for an unsolvable board
@given('an unsolvable Sudoku board')
def step_impl(context):
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '5', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    context.sudoku = Sudoku(board, 9, 9)

@when('the solver attempts to solve the board')
def step_impl(context):
    try:
        context.result = context.sudoku.solve()
        context.exception = None  # Clear any previous exception stored
    except Exception as e:
        context.exception = e  # Store the exception to verify later

@then('the board should be solved correctly')
def step_impl(context):
    assert context.result == True

@then('the solver should indicate the puzzle is unsolvable')
def step_impl(context):
    assert context.result == False

