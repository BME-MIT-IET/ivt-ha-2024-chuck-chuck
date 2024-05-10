from behave import *

from algorithms.bfs import shortest_distance


@given('a grid with buildings and empty spaces')
def step_impl(context):
    context.grid = [
        [1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]

@given('a grid with buildings but no empty spaces')
def step_impl(context):
    context.grid = [
        [1, 2, 1],
        [2, 1, 2]
    ]

@when('calculating the shortest distance to all buildings')
def step_impl(context):
    context.result = shortest_distance(context.grid)

@then('the shortest distance should be calculated correctly')
def step_impl(context):
    assert context.result == 7, "Expected 7, but got {}".format(context.result)


@then('the result should be -1 as there are no empty spaces')
def step_impl(context):
    assert context.result == -1, "Expected -1 for no empty spaces, but got {}".format(context.result)
